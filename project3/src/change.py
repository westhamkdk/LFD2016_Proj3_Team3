import time
import numpy as np
from scipy import zeros
import pandas as pd
import copy
from pybrain.rl.environments.twoplayergames.gomoku import GomokuGame
from lxml import etree
import pickle
import cPickle

import utility

class DataLoader(object):
    def __init__(self, model_type):
        self.load_episodes()
        self.episode_size = len(self.episodes)
        self.preload_episode_size = self.episode_size 
        self.current_episode_id = 0
        self.data_idx = 0
        self.file_idx = 1
        self.model_type = model_type
        self.preload_dataset()

    def load_episodes(self):
        file_path = '../data/renjunet_v10_20160425.rif'
        st = time.time()
        try:
            with open('../data/episodes.p', 'rb') as handle:
                print "pickle loaded"
                self.episodes = cPickle.load(handle)
                print "pickle loading complete"
        except Exception as e:
            print e
            print "failed to load episodes"
            self.episodes = utility.read_gomoku(file_path)

            print self.episodes[1]

            with open('../data/episodes.p', 'wb') as handle:
                cPickle.dump(self.episodes, handle)
        print time.time() - st

    def preload_dataset(self):
        if self.file_idx <= 9:
            self.preload_kibo = np.load('../data/kibo_%d.npy' %self.file_idx)
            if self.model_type == 'regression':
                self.preload_kibo = -self.preload_kibo

            self.preload_pos = np.load('../data/pos_%d.npy' %self.file_idx)
            self.preload_reward = np.load('../data/reward_%d.npy' %self.file_idx)

            if self.file_idx == 1:
                self.full_kibo = self.preload_kibo
                self.full_pos = self.preload_pos
                self.full_reward = self.preload_reward
            else:
                self.full_kibo = np.concatenate((self.full_kibo, self.preload_kibo))
                self.full_pos = np.concatenate((self.full_pos, self.preload_pos))
                self.full_reward = np.concatenate((self.full_reward, self.preload_reward))

            self.file_idx += 1

        else:
            self.preload_kibo = self.full_kibo
            self.preload_pos = self.full_pos
            self.preload_reward = self.full_reward


    def generate_batch(self, batch_size):
        epoch_over = False
        try:
            self.preload_kibo[self.data_idx + batch_size]
        except IndexError as e:
            print "indexError"
            self.preload_dataset()
            self.shuffle_data()
            self.data_idx = 0
            if self.file_idx >=10:
                epoch_over = True

        if self.model_type == "classification":
            batch_x = self.preload_kibo[self.data_idx:self.data_idx + batch_size]
            batch_y = self.preload_pos[self.data_idx:self.data_idx + batch_size]
        else:
            batch_x = self.preload_kibo[self.data_idx:self.data_idx + batch_size]
            batch_y = self.preload_reward[self.data_idx:self.data_idx + batch_size]

        self.data_idx += batch_size

        return batch_x, batch_y, epoch_over

    def shuffle_data(self):
        print "shuffle"
        random_idx = np.random.choice(range(len(self.preload_kibo)), len(self.preload_kibo), replace=False)
        self.preload_kibo = self.preload_kibo[random_idx, :]
        self.preload_pos = self.preload_pos[random_idx, :]
        self.preload_reward = self.preload_reward[random_idx, :]

    def cal_action_num(self, temp):
        cal = temp[0] * 15 + temp[1]
        return cal

    def make_reward_table(self, epi_num):
        epi = self.episodes[epi_num]
        reward = []

        for b in range(epi['reward'].size-1):
            reward.append(epi.values[b][5])

        return np.array(reward)

    def make_pos_table(self, epi_num):  # 0~14
        pos = []
        epi = self.episodes[epi_num]

        for a in range(epi['action'].size-1):
            temp = epi.values[a+1][4]
            cal = self.cal_action_num(temp)
            pos.append(cal)
        return np.array(pos)

    def make_kibo_panel(self, epi_num):

        epi = self.episodes[epi_num]

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
            full_mat.append(copy.deepcopy(temp))

        return np.array(full_mat)

    def get_kibo_pos_value(self, epi_num):
        return self.make_kibo_panel(epi_num), self.make_pos_table(epi_num), self.make_reward_table(epi_num)

if __name__ == '__main__':
    data_loader = DataLoader(model_type="classification")

    # type index number to get kibo, position and reward
    # print data_loader.get_kibo_pos_value(0)