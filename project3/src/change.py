import time
import numpy as np
from scipy import zeros
import pandas as pd

from pybrain.rl.environments.twoplayergames.gomoku import GomokuGame
from lxml import etree

import utility


def cal_action_num(temp):
    cal = temp[0] * 15 + temp[1]
    return cal

def make_reward_table(epi):
    reward = []

    for b in range(epi[0]['reward'].size):
        reward.append(epi[0].values[b][5])

    return reward

def make_pos_table(epi):  # 0~14
    pos = []
    for a in range(epi[0]['action'].size):
        temp = epi[0].values[a][4]
        cal = cal_action_num(temp)
        pos.append(cal)
    return pos

def make_real_pos_table(epi):
    matrix = [[[0 for col in range(15)] for row in range(15)]for dim in range(epi[0]['action'].size)]
    temp = [[0 for col in range(15)] for row in range(15)]

    for a in range(epi[0]['action'].size):
        cal = epi[0].values[a][4]
        if a % 2 == 0:
            temp[cal[0]][cal[1]] = 1
        elif a % 2 == 1:
            temp[cal[0]][cal[1]] = -1

        for row in range(15):
            print temp[row]

        print
        matrix.append(temp)

    return matrix


if __name__ == '__main__':
    file_path = '../data/renjunet_v10_20160425.rif'
    st = time.time()
    episodes = utility.read_gomoku(file_path)
    print time.time() - st

    # print episodes[0]
    # print episodes[0].values[0][5]
    # print episodes[0].index
    print episodes[0]['reward'].size
    # print episodes[0].values

    for a in range(episodes[0]['action'].size):
        if 0 in episodes[0].values[a][4]:
            print episodes[0].values[a][4]
            temp = episodes[0].values[a][4]

            print temp[0]

    print make_reward_table(episodes)
    print make_pos_table(episodes)

    print make_real_pos_table(episodes)







