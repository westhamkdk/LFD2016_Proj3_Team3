import cPickle as pickle
from collections import defaultdict
import random

from pybrain.rl.environments.twoplayergames.gomoku import GomokuGame
from pybrain.rl.environments.twoplayergames.gomokuplayers import randomplayer, killing

from player import n_Q_gomoku_player


# for testing
team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
MODULE_PATH = '../result/%d_module.pkl'

# size = (15, 15), dataset is renju
env = GomokuGame((15,15)) # env.b: state

# # play gomoku game
# # example
# p1 = killing.KillingGomokuPlayer(env) # player 1
# p2 = randomplayer.RandomGomokuPlayer(env, color=GomokuGame.WHITE) # player 2
#
# # play until the end
# env.playToTheEnd(p1, p2)
#
# if env.winner == p1.color:
#     print 'win player1!'
# elif env.winner == p2.color:
#     print 'win player2!'
# else:
#     print 'draw!'


# fight with own players
# load module
# module1 = pickle.load(MODULE_PATH % 1)
# module2 = pickle.load(MODULE_PATH % 2)

# fight!
win = []
lose = []
draw = []
soo2 = []
for i in range(10):
    p1 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
    # p2 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
    p2 = randomplayer.RandomGomokuPlayer(env, color=GomokuGame.BLACK) # player 2
    # p2 = killing.KillingGomokuPlayer(env, color=GomokuGame.BLACK) # player 1

    env.playToTheEnd(p1, p2)

    if env.winner == p1.color:
        win.append(1)
        print 'win player1!'
    elif env.winner == p2.color:
        lose.append(1)
        print 'win player2!'
    else:
        print 'draw!'
        draw.append(1)
    soo2.append(env.movesDone)

    env.reset()

print "win : ", sum(win), " / lose : ", sum(lose), " / draw : ", sum(draw)
print "average pansoo : ", sum(soo2)/10.0
## for test, TA
# score = defaultdict(int)
# for i in team:
#     for j in range(i+1, 13):
#         module1 = pickle.load(MODULE_PATH % i)
#         module2 = pickle.load(MODULE_PATH % j)
#
#         # select color
#         if random.random() < 0.5:
#             sun = [GomokuGame.BLACK, GomokuGame.WHITE]
#             black = 1
#         else:
#             sun = [GomokuGame.WHITE, GomokuGame.BLACK]
#             black = 2
#
#         for k in range(3):
#             player1 = n_Q_gomoku_player(module1, env, sun[0])
#             player2 = n_Q_gomoku_player(module2, env, sun[1])
#
#             # first one should be black
#             if player1.color == GomokuGame.BLACK:
#                 env.playToTheEnd(player1, player2)
#             else:
#                 env.playToTheEnd(player2, player1)
#
#             # score
#             if env.winner == player1.color:
#                 score[i] += 1
#             elif env.winner == player2.color:
#                 score[j] += 1
#
#             sun = -sun
#             env.reset()

