import cPickle as pickle
from collections import defaultdict
import random

from pybrain.rl.environments.twoplayergames.gomoku import GomokuGame
from pybrain.rl.environments.twoplayergames.gomokuplayers import randomplayer, killing

from player import n_Q_gomoku_player


env = GomokuGame((15,15)) # env.b: state

def rl_random_b():
    # fight!
    win = []
    lose = []
    draw = []
    soo2 = []
    for _ in range(10):
        p1 = n_Q_gomoku_player(None, env, GomokuGame.BLACK)
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
        p2 = randomplayer.RandomGomokuPlayer(env, color=GomokuGame.WHITE) # player 2
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.BLACK)
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

    print "win : "+str(sum(win))
    print "lose : "+str(sum(lose))
    print "draw : "+str(sum(draw))
    print "average pansoo : "+str(sum(soo2)/10.0)
    # return str("win : ", sum(win), " / lose : ", sum(lose), " / draw : ", sum(draw), "average pansoo : ", sum(soo2)/10.0)


def rl_random_w():
    # fight!
    win = []
    lose = []
    draw = []
    soo2 = []

    for _ in range(10):

        p1 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
        p2 = randomplayer.RandomGomokuPlayer(env, color=GomokuGame.BLACK) # player 2
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.BLACK)
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

    return str("win : ", sum(win), " / lose : ", sum(lose), " / draw : ", sum(draw), "average pansoo : ", sum(soo2)/10.0)

def rl_killing_w():
    # fight!
    win = []
    lose = []
    draw = []
    soo2 = []

    for _ in range(10):

        p1 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
        # p2 = randomplayer.RandomGomokuPlayer(env, color=GomokuGame.BLACK) # player 2
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.BLACK)
        p2 = killing.KillingGomokuPlayer(env, color=GomokuGame.BLACK) # player 1

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

    print str("win : ", sum(win), " / lose : ", sum(lose), " / draw : ", sum(draw), "average pansoo : ", sum(soo2)/10.0)


def rl_killing_b():
    # fight!
    win = []
    lose = []
    draw = []
    soo2 = []

    for _ in range(10):

        p1 = n_Q_gomoku_player(None, env, GomokuGame.BLACK)
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
        # p2 = randomplayer.RandomGomokuPlayer(env, color=GomokuGame.BLACK) # player 2
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.BLACK)
        p2 = killing.KillingGomokuPlayer(env, color=GomokuGame.WHITE) # player 1

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

    return str("win : ", sum(win), " / lose : ", sum(lose), " / draw : ", sum(draw), "average pansoo : ", sum(soo2)/10.0)

def rl_rl():
    # fight!
    win = []
    lose = []
    draw = []
    soo2 = []

    for _ in range(10):

        p1 = n_Q_gomoku_player(None, env, GomokuGame.BLACK)
        p2 = n_Q_gomoku_player(None, env, GomokuGame.WHITE)
        # p2 = randomplayer.RandomGomokuPlayer(env, color=GomokuGame.BLACK) # player 2
        # p2 = n_Q_gomoku_player(None, env, GomokuGame.BLACK)
        # p2 = killing.KillingGomokuPlayer(env, color=GomokuGame.WHITE) # player 1

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

    return str("win : ", sum(win), " / lose : ", sum(lose), " / draw : ", sum(draw), "average pansoo : ", sum(soo2)/10.0)

if __name__ == '__main__':
    print "rl(black) vs random"
    print rl_random_b()
    # print "rl(white) vs random"
    # print rl_random_w()
    #
    # print "rl(black) vs killing"
    # print rl_killing_b()
    # print "rl(white) vs killing"
    # print rl_killing_w()
    #
    # print "rl vs rl"
    # rl_rl()