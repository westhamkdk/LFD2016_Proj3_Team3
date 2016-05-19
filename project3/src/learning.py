from pybrain.rl.environments.twoplayergames.gomokuplayers.gomokuplayer import GomokuPlayer, GomokuGame
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.agents import LearningAgent
from pybrain.datasets.reinforcement import ReinforcementDataSet

import cPickle as pickle
from utility import read_gomoku


# for saving model
MODEL_DIR = '../model/%s_module.pkl'
team_number = '1' # change for your team name

# for learning model
# change for your model
STATE_DIM = 1
ACTION_DIM = 1

environment = GomokuGame((15, 15))
# if you want to make own Q function, then make a new class that inherits ActionValueInterface
controller = ActionValueTable(15*15+1, 15*15) # change dimension along your definition, for Q-learning algorithm
controller.initialize(1.)

file_path = '../data/renjunet_v10_20160425.rif'
episodes = read_gomoku(file_path)

dataset = ReinforcementDataSet(STATE_DIM, ACTION_DIM)
for episode in episodes:
    for i, row in episode.iterrows():
        print i, type(row['state'])
        dataset.addSample(row['state'], environment.convertPosToIndex(row['action']), row['reward'])
        print dataset.data['state']
    dataset.newSequence()

learner = Q()
agent = LearningAgent(controller, learner)
agent.learner.dataset = dataset
agent.learn()

f = open(MODEL_DIR % team_number, 'wb')
pickle.dump(controller, f)