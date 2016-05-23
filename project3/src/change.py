import time
import numpy as np
from scipy import zeros
import pandas as pd

from pybrain.rl.environments.twoplayergames.gomoku import GomokuGame
from lxml import etree
import pickle
import cPickle

import utility


def cal_action_num(temp):
    cal = temp[0] * 15 + temp[1]
    return cal

def make_reward_table(epi_num):
    epi = episodes[epi_num]
    reward = []

    for b in range(epi['reward'].size-1):
        reward.append(epi.values[b][5])

    return np.array(reward)

def make_pos_table(epi_num):  # 0~14
    pos = []
    epi = episodes[epi_num]

    for a in range(epi['action'].size-1):
        temp = epi.values[a+1][4]
        cal = cal_action_num(temp)
        pos.append(cal)
    return np.array(pos)

def make_kibo_panel(epi_num):

    epi = episodes[epi_num]

    new_dict = dict()
    temp = [[0 for col in range(15)] for row in range(15)]

    full_mat = []
    for a in range(epi['action'].size-1):

        cal = epi.values[a][4]

        if a % 2 == 0:
            temp[cal[0]][cal[1]] = 1
        elif a % 2 == 1:
            temp[cal[0]][cal[1]] = -1

        df = pd.DataFrame(temp)
        new_dict[a] = df
        full_mat.append(temp)

    print np.array(full_mat)
    return np.array(full_mat)

def get_kibo_pos_value(epi_num):
    return make_kibo_panel(epi_num), make_pos_table(epi_num), make_reward_table(epi_num)
    
def change_kibo_simple(state):

    pannel = [[0 for col in range(15)] for row in range(15)]

    for a in range(len(state)):
        if a % 2 == 0 and state[a] == 1:  # black
            pannel[(a/2) / 15][(a/2) % 15] = 1
        elif a % 2 == 1 and state[a] == 1:  # white
            pannel[(a/2) / 15][(a/2) % 15] = -1

    return pannel

if __name__ == '__main__':
    file_path = '../data/renjunet_v10_20160425.rif'
    st = time.time()

    # episodes' index are sequential
    try:
        with open('../data/episodes.p', 'rb') as handle:
            print "pickle loaded"
            episodes = cPickle.load(handle)
    except Exception as e:
        print e
        print "failed to load episodes"
        episodes = utility.read_gomoku(file_path)

        with open('../data/episodes.p', 'wb') as handle:
            cPickle.dump(episodes, handle)


    # type index number to get kibo, position and reward
    print get_kibo_pos_value(0)

    #print time.time() - st











