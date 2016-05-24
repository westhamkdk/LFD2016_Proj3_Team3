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
        self.preload_dataset()
        self.model_type = model_type
        self.file_idx = file_idx
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
                    self.preload_kibo, self.preload_pos, self.preload_reward = self.get_kibo_pos_value(episode_id)
                else:
                    kibo, pos, reward = self.get_kibo_pos_value(episode_id)
                    if episode_id % 50 == 0:
                        print "episodo id : ", str(episode_id), "/", str(self.episode_size)
                    try:
                        self.preload_kibo = np.concatenate((self.preload_kibo, kibo))
                        self.preload_pos = np.concatenate((self.preload_pos, pos))
                        self.preload_reward = np.concatenate((self.preload_reward, reward))
                    except Exception as e:
                        print e
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

if __name__ == '__main__':
    data_loader = DataLoader(model_type="classification", file_idx=9)