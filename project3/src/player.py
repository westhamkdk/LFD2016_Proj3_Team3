from cnn import CNN
from pybrain.rl.environments.twoplayergames.gomokuplayers.gomokuplayer import GomokuPlayer
from random import choice
import numpy as np
import copy
import os
import tensorflow as tf

class n_Q_gomoku_player(GomokuPlayer):
    """
    change n to your team number
    """

    def __init__(self, module, game, color, **args):
        self.module = module
        self.game = game
        self.color = color
        self.setArgs(**args)

    def getAction(self):
        ## TODO
        """
        get suggested action, and it should be legal
        return [self.color, suggested_action]
        """
        ba = self.game.getBoardArray()
        state = self.game.invertBoardArray(ba)

        if self.color == 1:
            print "I'm BLACK stone"
        elif self.color == -1:
            print "I'm White stone"
        else:
            raise Exception("self.color is either 1 or -1, current color is %d"%self.color)

        panel = self.change_kibo_simple(state)
        possible_move, possible_pos = self.get_available_counts(panel, self.color)

        print "---------------"
        print self.color
        print state.sum()
        print state[::2].sum()
        print state[1::2].sum()
        print state
        print panel
        print possible_move
        print possible_pos

        ## if there is a rule then change possible_move
        # e.g. possible_move = by_sum_rule(possible_move)
        # or directly change 'get_available_counts' funtion

        # values = self.get_values(possible_move)
        # print values.shape
        # if self.color == 1:
        #     highest_value_idx = np.argmax(values)
        #     best_pos = possible_pos[highest_value_idx]
        # elif self.color == -1:
        #     lowest_value_idx = np.argmin(values)
        #     best_pos = possible_pos[lowest_value_idx]
        #
        # action = self._convertIndexToPos(best_pos)
        action = (0, 0)
        if self.game.isLegal(self.color, action):
            print "legal move"
            return [self.color, action]
        else:
            print "ilegal move"
            return [self.color, choice(self.game.getLegals(self.color))]


    def _convertIndexToPos(self, i):
        ## TODO: change for your state or board position definition
        # convert state vector to position in gomoku e.g. 80 -> (5,5)
        return (i//self.game.size[0], i%self.game.size[0])

    def _convertPosToIndex(self, p):
        ## TODO: change for your state or board position definition
        # convert position to index in gomoku e.g. (5,5) - > 80
        return p[0]*self.game.size[0]+p[1]

    def integrateObservation(self, obs=None):
        pass

    def newEpisode(self):
        self.module.reset()


    def change_kibo_simple(self, state):

        pannel = [[0 for col in range(15)] for row in range(15)]

        for a in range(len(state)):
            if a % 2 == 0 and state[a] == 1:  # black
                pannel[(a/2) / 15][(a/2) % 15] = 1
            elif a % 2 == 1 and state[a] == 1:  # white
                pannel[(a/2) / 15][(a/2) % 15] = -1

        return pannel

    def get_available_counts(self, current_panel, color):
        full_mat = []
        pos = []
        next_dol = 0
        if color == 1:
            next_dol = 1
        elif color == -1:
            next_dol = -1

        for i in range(0,15):
            for j in range(0,15):
                temp = copy.deepcopy(current_panel)
                if temp[i][j] == 0:
                    temp[i][j] = next_dol
                    full_mat.append(temp)
                    pos.append(i*15 + j)
        return np.array(full_mat), np.array(pos)

    def get_values(self, possible_move):
        # Parameters
        learning_rate = 0.00005
        training_iters = 100
        batch_size = 128
        display_step = 50
        n_input = 15 * 15  # MNIST data input (img shape: 28*28)
        n_classes = 225  # MNIST total classes (0-9 digits)
        model_type = "regression"
        with tf.Session() as sess:
            cnn = CNN(sess, learning_rate, training_iters, batch_size, display_step, n_input, n_classes,
                      model_type=model_type)
            return cnn.inference(possible_move)