import numpy as np
from scipy import zeros
import pandas as pd

from pybrain.rl.environments.twoplayergames.gomoku import GomokuGame
from lxml import etree

import time


# you should determine the number of gibo.
# I recommend that you load all gibos and save using pickle
def read_gomoku(file_path):
    episodes = []
    with open(file_path, 'rb') as f:
        root = etree.parse(f)

        idx = 1
        for element in root.iter('game'):
            print idx
            result = element.attrib.get('bresult')
            sequence = element.getchildren()[0].text.split(' ')
            if len(result) < 1 or len(sequence) < 1:
                break

            episode = gen_episode(result, sequence, idx)
            episodes.append(episode)

            idx += 1

    return episodes


## TODO: change for your state definition
def convertStateToIdx(state):

    pass


## TODO: change for your state definition
def convertIdxToState(Idx):

    pass


## TODO definition of state
def state_from_ba(ba):

    state = sum(ba)

    return state


## TODO definition of reward
def reward_from_result(bresult):
    if bresult == 1.:
        breward = 1
        wreward = -1
    elif bresult == 0.5:
        breward = 0
        wreward = 0
    else:
        breward = -1
        wreward = 1

    return breward, wreward


def gen_episode(result, sequence, idx):

    env = GomokuGame((15, 15))
    episode = pd.DataFrame(columns=['episode_id', 'turn_id', 'color', 'state', 'action', 'reward']) # change if you want

    bresult = np.float16(result) # reward for black
    breward, wreward = reward_from_result(bresult)

    color = GomokuGame.BLACK
    for i, position in enumerate(sequence):
        if len(position) == 0:
            break
        row = ord(position[0])-97
        column = int(position[1:])-1
        ba = env.getBoardArray()

        ## TODO change state strategy.
        if i%2 != 0:
            # invert values ( same input structure for both white and balck)
            ba = env.invertBoardArray(ba)
            reward = wreward
        else:
            reward = breward

        state = state_from_ba(ba)

        ## TODO change if you want more information e.g. next state
        episode = episode.append(pd.Series({'episode_id': idx, 'turn_id': i+1, 'color': color, 'state': state,
                                            'action': (row, column), 'reward': reward}), ignore_index=True)

        env.doMove(color, (row, column))
        color = -color

    return episode


if __name__ == '__main__':
    file_path = '../data/renjunet_v10_20160425.rif'
    st = time.time()
    episodes = read_gomoku(file_path)
    print time.time() - st
    print episodes[0]
    print len(episodes)
