from pybrain.rl.environments.twoplayergames.gomokuplayers.gomokuplayer import GomokuPlayer
from random import choice

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
        print "---------------"
        print self.color
        print state.sum()
        print state[::2].sum()
        print state[1::2].sum()
        print state


        # action = self.module.getMaxAction()

        action = (0,0)
        if self.game.isLegal(self.color, action):
            return [self.color, action]
        else:
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

