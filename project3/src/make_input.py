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
    def __init__(self, model_type, file_idx):
        self.load_episodes()
        self.episode_size = len(self.episodes)
        self.preload_episode_size = self.episode_size
        self.current_episode_id = 0
        self.data_idx = 0
        self.file_idx = file_idx
        self.preload_dataset()
        self.model_type = model_type
        print self.episode_size

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

            with open('../data/episodes.p', 'wb') as handle:
                cPickle.dump(self.episodes, handle)
        print time.time() - st

    def preload_dataset(self):
        try:
            self.preload_kibo = np.load('../data/kibo.npy')
            self.preload_pos = np.load('../data/pos.npy')
            self.preload_reward = np.load('../data/reward.npy')
        except Exception as e:
            print e
            self.preload_kibo, self.preload_pos, self.preload_reward = None, None, None

            for episode_id in range((self.file_idx-1)*5000 +1,
                                    min(self.file_idx*5000+1, self.episode_size)):
                if self.preload_kibo is None:
                    self.preload_kibo, self.preload_pos, self.preload_reward, color = self.get_kibo_pos_value(episode_id)
                    # self.preload_reward = np.array([self.preload_reward[0]]*self.preload_reward.shape[0])
                    # print self.preload_kibo[10]
                    # print self.preload_kibo[11]
                    # print color
                    self.preload_kibo =  self.preload_kibo * color.reshape((color.shape[0], 1, 1))
                    # print self.preload_kibo[10]
                    # print self.preload_kibo[11]
                else:
                    kibo, pos, reward, color = self.get_kibo_pos_value(episode_id)
                    if episode_id % 50 == 0:
                        print "episodo id : ", str(episode_id), "/", str(self.episode_size)
                    try:
                        print kibo[0], pos[0], color[0]
                        print kibo[1], pos[1], color[1]
                        print kibo[2], pos[2], color[2]
                        print kibo[3], pos[3], color[3]
                        print color
                        kibo = kibo * color.reshape((color.shape[0], 1, 1))
                        print kibo[0], pos[0], color[0]
                        print kibo[1], pos[1], color[1]
                        print kibo[2], pos[2], color[2]
                        print kibo[3], pos[3], color[3]
                        self.preload_kibo = np.concatenate((self.preload_kibo, kibo))
                        self.preload_pos = np.concatenate((self.preload_pos, pos))
                        self.preload_reward = np.concatenate((self.preload_reward, reward))
                    except Exception as e:
                        print e
                        print reward
                        print self.preload_kibo
                        print kibo

#            self.current_episode_id += self.preload_episode_size
#            if self.current_episode_id >=self.episode_size:
#                self.current_episode_id = 0

                assert len(self.preload_kibo) == len(self.preload_pos) == len(self.preload_reward)
                if (episode_id != 0 and episode_id % 5000 == 0) or (episode_id ==(self.episode_size-1)):
                    self.preload_kibo = np.reshape(self.preload_kibo, (self.preload_kibo.shape[0], 15, 15, 1))
                    temp_pos = np.zeros(shape=(self.preload_pos.shape[0], 225))
                    temp_pos[:, self.preload_pos] = 1
                    self.preload_pos = temp_pos
                    self.preload_reward = np.reshape(self.preload_reward, (self.preload_reward.shape[0], 1))

                    print "saving..."
                    idx = episode_id // 5000
                    if episode_id == (self.episode_size-1):
                        idx += 1
                    np.save('../data/kibo_%d' %idx, self.preload_kibo)
                    np.save('../data/pos_%d' %idx, self.preload_pos)
                    np.save('../data/reward_%d' %idx, self.preload_reward)
                    self.preload_kibo, self.preload_pos, self.preload_reward = None, None, None
                    print "saving complete"


    def cal_action_num(self, temp):
        cal = temp[0] * 15 + temp[1]
        return cal


    def make_reward_table(self, epi_num):
        epi = self.episodes[epi_num]
        reward = []

        for b in range(epi['reward'].size - 1):
            reward.append(epi.values[b][5])

        return np.array(reward)


    def make_pos_table(self, epi_num):  # 0~14
        pos = []
        epi = self.episodes[epi_num]

        for a in range(epi['action'].size - 1):
            temp = epi.values[a + 1][4]
            cal = self.cal_action_num(temp)
            pos.append(cal)
        return np.array(pos)

    def get_color(self, epi_num):
        return self.episodes[epi_num]['color'].as_matrix()[:-1]

    def make_kibo_panel(self, epi_num):
        epi = self.episodes[epi_num]

        new_dict = dict()
        temp = [[0 for col in range(15)] for row in range(15)]

        full_mat = []
        for a in range(epi['action'].size - 1):

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
        return self.make_kibo_panel(epi_num), self.make_pos_table(epi_num), self.make_reward_table(epi_num), self.get_color(epi_num)

if __name__ == '__main__':
    data_loader = DataLoader(model_type="classification", file_idx=1)