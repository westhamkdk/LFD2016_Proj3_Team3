import numpy as np
import copy


def count_attack_defend(current_panel):
    return attack_finish(current_panel)

def attack_finish(current_panel):
    # find next position that can win the game
    temp_panel = copy.deepcopy(current_panel)
    # oppo = -1
    mine = 1
    full_mat = []
    pos = []

    # priority 1
    # width 4
    for i in range(0, 15):
        for j in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 2] == mine and \
                            temp_panel[i][j + 3] == mine:
                # left-end
                if (j == 0):
                    if temp_panel[i][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 4] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 4)
                # right-end
                elif (j == 11):
                    if temp_panel[i][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j - 1] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j - 1)
                # others
                else:
                    if temp_panel[i][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j - 1] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j - 1)

                    if temp_panel[i][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 4] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 4)
    # height 4
    for j in range(0, 15):
        for i in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 2][j] == mine and \
                            temp_panel[i + 3][j] == mine:

                # top-end
                if (i == 0):
                    if temp_panel[i + 4][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j] = mine
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j)

                # bottom-end
                elif (i == 11):
                    if temp_panel[i - 1][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j)

                # others
                else:
                    if temp_panel[i + 4][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j] = mine
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j)

                        if temp_panel[i - 1][j] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j] = mine
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j)
    # diagonal 4
    for i in range(0, 12):
        for j in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 2][j + 2] == mine and \
                            temp_panel[i + 3][j + 3] == mine:

                tf_check_rb = False
                tf_check_lt = False

                # left or top end
                if (i == 0 or j == 0):
                    tf_check_rb = True
                # right or bottom end
                elif (i == 11 or j == 11):
                    tf_check_lt = True
                else:
                    tf_check_lt = True
                    tf_check_rb = True

                if (tf_check_rb):
                    if temp_panel[i + 4][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j + 4] = mine
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j + 4)

                if (tf_check_lt):
                    if temp_panel[i - 1][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j - 1] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j - 1)
    for i in range(0, 12):
        for j in range(0, 12):
            if temp_panel[i][j + 3] == mine and temp_panel[i + 1][j + 2] == mine and temp_panel[i + 2][
                        j + 1] == mine and temp_panel[i + 3][j] == mine:
                tf_check_rt = False
                tf_check_lb = False

                # right or top end
                if (i == 0 or j == 11):
                    tf_check_lb = True
                # left or bottom end
                elif (i == 11 or j == 0):
                    tf_check_rt = True
                else:
                    tf_check_rt = True
                    tf_check_lb = True

                if (tf_check_rt):
                    if temp_panel[i - 1][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j + 4] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j + 4)

                if (tf_check_lb):
                    if temp_panel[i + 4][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j - 1] = mine
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j - 1)

    # width 2-2, 3-1, 1-3
    for i in range(0, 15):
        for j in range(0, 11):
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 3] == mine and \
                            temp_panel[i][j + 4] == mine:
                if temp_panel[i][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 2] = mine
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 2)
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 2] == mine and \
                            temp_panel[i][j + 4] == mine:
                if temp_panel[i][j + 3] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 3] = mine
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 3)
            if temp_panel[i][j] == mine and temp_panel[i][j + 2] == mine and temp_panel[i][j + 3] == mine and \
                            temp_panel[i][j + 4] == mine:
                if temp_panel[i][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 1] = mine
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 1)
    # height 2-2, 3-1, 1-3
    for j in range(0, 15):
        for i in range(0, 11):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 3][j] == mine and \
                            temp_panel[i + 4][j] == mine:
                if temp_panel[i + 2][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j] = mine
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j)
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 2][j] == mine and \
                            temp_panel[i + 4][j] == mine:
                if temp_panel[i + 3][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 3][j] = mine
                    full_mat.append(temp)
                    pos.append((i + 3) * 15 + j)
            if temp_panel[i][j] == mine and temp_panel[i + 2][j] == mine and temp_panel[i + 3][j] == mine and \
                            temp_panel[i + 4][j] == mine:
                if temp_panel[i + 1][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j] = mine
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j)
    # diagonal
    for i in range(0, 11):
        for j in range(0, 11):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 2][j + 2] == mine and \
                            temp_panel[i + 4][j + 4] == mine:
                if temp_panel[i + 3][j + 3] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 3][j + 3] = mine
                    full_mat.append(temp)
                    pos.append((i + 3) * 15 + j + 3)
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 3][
                        j + 3] == mine and temp_panel[i + 4][j + 4] == mine:
                if temp_panel[i + 2][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j + 2] = mine
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j + 2)
            if temp_panel[i][j] == mine and temp_panel[i + 2][j + 2] == mine and temp_panel[i + 3][
                        j + 3] == mine and temp_panel[i + 4][j + 4] == mine:
                if temp_panel[i + 1][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j + 1] = mine
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j + 1)
    for i in range(0, 11):
        for j in range(0, 11):
            if temp_panel[i][j + 4] == mine and temp_panel[i + 1][j + 3] == mine and temp_panel[i + 2][
                        j + 2] == mine and temp_panel[i + 4][j] == mine:
                if temp_panel[i + 3][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 3][j + 1] = mine
                    full_mat.append(temp)
                    pos.append((i + 3) * 15 + j + 1)
            if temp_panel[i][j + 4] == mine and temp_panel[i + 1][j + 3] == mine and temp_panel[i + 3][
                        j + 1] == mine and temp_panel[i + 4][j] == mine:
                if temp_panel[i + 2][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j + 2] = mine
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j + 2)
            if temp_panel[i][j + 4] == mine and temp_panel[i + 2][j + 2] == mine and temp_panel[i + 3][
                        j + 1] == mine and temp_panel[i + 4][j] == mine:
                if temp_panel[i + 1][j + 3] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j + 3] = mine
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j + 3)

    if pos != []:
        return np.array(full_mat), np.array(pos)
    else:
        return defend_finish(current_panel)

def attack_checkmate(current_panel):
    # find next position that can win the game
    temp_panel = copy.deepcopy(current_panel)
    # oppo = -1
    mine = 1
    full_mat = []
    pos = []

    # priority 2
    # width xooxox or xoxoox
    for i in range(0, 15):
        for j in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 3] == mine:
                # check if both sides are playable
                # empty or not deadend
                if (j > 0 and j < 11):
                    if (temp_panel[i][j - 1] == 0 and temp_panel[i][j + 4] == 0):
                        if temp_panel[i][j + 2] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 2] = mine
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 2)

            if temp_panel[i][j] == mine and temp_panel[i][j + 2] == mine and temp_panel[i][j + 3] == mine:
                # check if both sides are playable
                # empty or not deadend
                if (j > 0 and j < 11):
                    if (temp_panel[i][j - 1] == 0 and temp_panel[i][j + 4] == 0):
                        if temp_panel[i][j + 1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 1] = mine
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 1)
    # height xooxox or xoxoox
    for j in range(0, 15):
        for i in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 3][j] == mine:
                if (i > 0 and i < 11):
                    if (temp_panel[i - 1][j] == 0 and temp_panel[i + 4][j] == 0):
                        if temp_panel[i + 2][j] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 2][j] = mine
                            full_mat.append(temp)
                            pos.append((i + 2) * 15 + j)
            if temp_panel[i][j] == mine and temp_panel[i + 2][j] == mine and temp_panel[i + 3][j] == mine:
                if (i > 0 and i < 11):
                    if (temp_panel[i - 1][j] == 0 and temp_panel[i + 4][j] == 0):
                        if temp_panel[i + 1][j] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 1][j] = mine
                            full_mat.append(temp)
                            pos.append((i + 1) * 15 + j)
    # diagonal
    for i in range(0, 12):
        for j in range(0, 12):
            # need to change
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 3][j + 3] == mine:
                # [i-1][j-1] and [i+4][j+4] considered
                if (i > 0 and i < 11) and (j > 0 and j < 11):
                    if (temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 4][j + 4] == 0):
                        if temp_panel[i + 2][j + 2] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 2][j + 2] = mine
                            full_mat.append(temp)
                            pos.append((i + 2) * 15 + j + 2)
            if temp_panel[i][j] == mine and temp_panel[i + 2][j + 2] == mine and temp_panel[i + 3][j + 3] == mine:
                # [i-1][j-1] and [i+4][j+4] considered
                if (i > 0 and i < 11) and (j > 0 and j < 11):
                    if (temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 4][j + 4] == 0):
                        if temp_panel[i + 1][j + 1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 1][j + 1] = mine
                            full_mat.append(temp)
                            pos.append((i + 1) * 15 + j + 1)
    for i in range(0, 12):
        for j in range(0, 12):
            if temp_panel[i + 3][j] == mine and temp_panel[i + 2][j + 1] == mine and temp_panel[i][j + 3] == mine:
                # [i-1][j+4] and [i+4][j-1] considered
                if (i > 0 and i < 11) and (j > 0 and j < 11):
                    if (temp_panel[i - 1][j + 4] == 0 and temp_panel[i + 4][j - 1] == 0):
                        if temp_panel[i + 1][j + 2] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 1][j + 2] = mine
                            full_mat.append(temp)
                            pos.append((i + 1) * 15 + j + 2)
            if temp_panel[i + 3][j] == mine and temp_panel[i + 1][j + 2] == mine and temp_panel[i][j + 3] == mine:
                # [i-1][j+4] and [i+4][j-1] considered
                if (i > 0 and i < 11) and (j > 0 and j < 11):
                    if (temp_panel[i - 1][j + 4] == 0 and temp_panel[i + 4][j - 1] == 0):
                        if temp_panel[i + 2][j + 1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 2][j + 1] = mine
                            full_mat.append(temp)
                            pos.append((i + 2) * 15 + j + 1)
    # width 3
    # need to change
    for i in range(0, 15):
        for j in range(1, 12):
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 2] == mine:

                # neighbor places should be empty
                if temp_panel[i][j - 1] == 0 and temp_panel[i][j + 3] == 0:  # xooox
                    # check whether blocked
                    # if j==1 --> it must be j+3
                    # if j==11 --> it must be j-1
                    tf_r_block = False
                    tf_l_block = False

                    if (j == 1):
                        tf_l_block = True
                    elif (j == 11):
                        tf_r_block = True

                    try:
                        if (temp_panel[i][j - 2] == -1):
                            tf_l_block = True
                    except:
                        pass

                    try:
                        if (temp_panel[i][j + 4] == -1):
                            tf_r_block = True
                    except:
                        pass

                    if (not tf_r_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 3] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 3)

                    if (not tf_l_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i][j - 1] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j - 1)

    # height over 3
    for j in range(0, 15):
        for i in range(1, 12):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 2][j] == mine:
                # neighbor places should be empty
                if temp_panel[i - 1][j] == 0 and temp_panel[i + 3][j] == 0:  # xooox
                    # check whether blocked
                    # if i==1 --> it must be i+3
                    # if i==11 --> it must be i-1
                    tf_b_block = False
                    tf_t_block = False

                    if (i == 1):
                        tf_t_block = True
                    elif (i == 11):
                        tf_b_block = True

                    try:
                        if (temp_panel[i - 2][j] == -1):
                            tf_t_block = True
                    except:
                        pass

                    try:
                        if (temp_panel[i + 4][j] == -1):
                            tf_b_block = True
                    except:
                        pass

                    if (not tf_b_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j] = mine
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j)

                    if (not tf_t_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j)

    # diagonal1
    for j in range(1, 12):
        for i in range(1, 12):
            # exclude edges
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 2][j + 2] == mine:
                if temp_panel[i + 3][j + 3] == 0 and temp_panel[i - 1][j - 1] == 0:  # xooox

                    tf_rb_block = False
                    tf_lt_block = False

                    # left or top
                    if (i == 1 or j == 1):
                        tf_lt_block = True
                    # right or bottom
                    elif (i == 11 or j == 11):
                        tf_rb_block = True

                    try:
                        if (temp_panel[i - 2][j - 2] == -1):
                            tf_lt_block = True
                    except:
                        pass
                    try:
                        if (temp_panel[i + 4][j + 4] == -1):
                            tf_rb_block = True
                    except:
                        pass

                    if (not tf_rb_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j + 3] = mine
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j + 3)

                    if (not tf_lt_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j - 1] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j - 1)
    # diagonal2
    for j in range(1, 12):
        for i in range(1, 12):
            # exclude edges
            if temp_panel[i + 2][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i][j + 2] == mine:
                if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:  # xooox
                    tf_rt_block = False
                    tf_lb_block = False

                    # right or top end
                    if (i == 1 or j == 11):
                        tf_rt_block = True
                    # left or bottom end
                    elif (i == 11 or j == 1):
                        tf_lb_block = True

                    try:
                        if (temp_panel[i + 4][j - 2] == -1):
                            tf_lb_block = True
                    except:
                        pass
                    try:
                        if (temp_panel[i - 2][j + 4] == -1):
                            tf_rt_block = True
                    except:
                        pass

                    if (not tf_lb_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j - 1] = mine
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j - 1)

                    if (not tf_rt_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j + 3] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j + 3)

    if pos != []:
        return np.array(full_mat), np.array(pos)
    else:
        return defend_others(current_panel)

def defend_finish(current_panel):
    #priority 1
    full_mat = []
    pos = []
    next_dol = 1
    next_dol2 = 1
    oppo = -1
    temp_panel = copy.deepcopy(current_panel)

    if next_dol == 1:
        # have to defense
        # priority 1

        # width 2-2, 3-1, 1-3
        for i in range(0, 15):
            for j in range(0, 11):
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 3] == oppo and \
                                temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and \
                                temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 3)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i][j + 3] == oppo and \
                                temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
        # height 2-2, 3-1, 1-3
        for j in range(0, 15):
            for i in range(0, 11):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 3][j] == oppo and \
                                temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 2][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 2][j] == oppo and \
                                temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 3][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i + 2][j] == oppo and temp_panel[i + 3][j] == oppo and \
                                temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 1][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j)
        # diagonal
        for i in range(0, 11):
            for j in range(0, 11):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][
                            j + 2] == oppo and temp_panel[i + 4][j + 4] == oppo:
                    if temp_panel[i + 3][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j + 3)
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 3][
                            j + 3] == oppo and temp_panel[i + 4][j + 4] == oppo:
                    if temp_panel[i + 2][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i + 2][j + 2] == oppo and temp_panel[i + 3][
                            j + 3] == oppo and temp_panel[i + 4][j + 4] == oppo:
                    if temp_panel[i + 1][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j + 1)
        for i in range(0, 11):
            for j in range(0, 11):
                if temp_panel[i][j + 4] == oppo and temp_panel[i + 1][j + 3] == oppo and temp_panel[i + 2][
                            j + 2] == oppo and temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 3][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j + 1)
                if temp_panel[i][j + 4] == oppo and temp_panel[i + 1][j + 3] == oppo and temp_panel[i + 3][
                            j + 1] == oppo and temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 2][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j + 2)
                if temp_panel[i][j + 4] == oppo and temp_panel[i + 2][j + 2] == oppo and temp_panel[i + 3][
                            j + 1] == oppo and temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 1][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j + 3)

        if pos != []:
            return np.array(full_mat), np.array(pos)
        else:
            return attack_checkmate(current_panel)

def defend_others(current_panel):
    full_mat = []
    pos = []
    next_dol = 1
    next_dol2 = 1
    oppo = -1

    temp_panel = copy.deepcopy(current_panel)

    # others
    # priority 2
    # width xooxox or xoxoox
    for i in range(0, 15):
        for j in range(1, 11):
            if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 3] == oppo and \
                            temp_panel[i][j + 2] == 0:
                if temp_panel[i][j + 4] == 0 and temp_panel[i][j - 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 2] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 2)
            if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i][j + 3] == oppo and \
                            temp_panel[i][j + 1] == 0:
                if temp_panel[i][j + 4] == 0 and temp_panel[i][j - 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 1] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 1)
    # height xooxox or xoxoox
    for j in range(0, 15):
        for i in range(1, 11):
            if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 3][j] == oppo and \
                            temp_panel[i + 2][j] == 0:
                if temp_panel[i + 4][j] == 0 and temp_panel[i - 1][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j] = next_dol2
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j)
            if temp_panel[i][j] == oppo and temp_panel[i + 2][j] == oppo and temp_panel[i + 3][j] == oppo and \
                            temp_panel[i + 1][j] == 0:
                if temp_panel[i + 4][j] == 0 and temp_panel[i - 1][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j] = next_dol2
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j)
    # diagonal
    for i in range(1, 11):
        for j in range(1, 12):
            if temp_panel[i][j] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 3][
                        j + 3] == oppo and temp_panel[i + 2][j + 2] == 0:
                if temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 4][j + 4] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j + 2] = next_dol2
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j + 2)
            if temp_panel[i][j] == oppo and temp_panel[i + 2][j + 2] == oppo and temp_panel[i + 3][
                        j + 3] == oppo and temp_panel[i + 1][j + 1] == 0:
                if temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 4][j + 4] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j + 1] = next_dol2
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j + 1)
    for i in range(1, 11):
        for j in range(1, 11):
            if temp_panel[i + 3][j] == oppo and temp_panel[i + 2][j + 1] == oppo and temp_panel[i][
                        j + 3] == oppo and temp_panel[i + 1][j + 2] == 0:
                if temp_panel[i + 4][j - 1] == 0 and temp_panel[i - 1][j + 4] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j + 2] = next_dol2
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j + 2)
            if temp_panel[i + 3][j] == oppo and temp_panel[i + 1][j + 2] == oppo and temp_panel[i][
                        j + 3] == oppo and temp_panel[i + 2][j + 1] == 0:
                if temp_panel[i + 4][j - 1] == 0 and temp_panel[i - 1][j + 4] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j + 1] = next_dol2
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j + 1)

    # width over 3
    for i in range(0, 15):
        for j in range(0, 13):
            if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo:
                if 12 > j > 0:
                    if temp_panel[i][j - 1] == 0 and temp_panel[i][j + 3] == 0:  # xooox
                        if j == 1:
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 3)
                        elif j == 11:
                            temp = copy.deepcopy(current_panel)
                            temp[i][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 1)
                        elif 1 < j < 11:
                            if temp_panel[i][j - 2] == 0 and temp_panel[i][j + 4] == next_dol:
                                temp = copy.deepcopy(current_panel)
                                temp[i][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append(i * 15 + j - 1)
                            elif temp_panel[i][j - 2] == next_dol and temp_panel[i][j + 4] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append(i * 15 + j + 3)
                            elif temp_panel[i][j - 2] == 0 and temp_panel[i][j + 4] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append(i * 15 + j - 1)

                                temp = copy.deepcopy(current_panel)
                                temp[i][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append(i * 15 + j + 3)

                    elif temp_panel[i][j - 1] == next_dol and temp_panel[i][j + 3] == oppo and j < 11:
                        if temp_panel[i][j + 4] == 0:  # Moooox
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 4)

                    elif temp_panel[i][j - 1] == oppo and temp_panel[i][j + 3] == next_dol and j > 2:
                        if temp_panel[i][j - 2] == 0:  # xooooM
                            temp = copy.deepcopy(current_panel)
                            temp[i][j - 2] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 2)
                elif j == 0:  # left end
                    if temp_panel[i][j + 3] == oppo and temp_panel[i][j + 4] == 0:  # 4
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 4] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 4)
                elif j == 12:  # right end
                    if temp_panel[i][j - 1] == oppo and temp_panel[i][j - 2] == 0:  # 4
                        temp = copy.deepcopy(current_panel)
                        temp[i][j - 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j - 2)
    # height over 3
    for j in range(0, 15):
        for i in range(0, 13):
            if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 2][j] == oppo:
                if 12 > i > 0:
                    if temp_panel[i - 1][j] == 0 and temp_panel[i + 3][j] == 0:  # both empty
                        if i == 1:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j)
                        elif i == 11:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j)
                        elif 1 < i < 11:
                            if temp_panel[i - 2][j] == 0 and temp_panel[i + 4][j] == next_dol:
                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j)
                            elif temp_panel[i - 2][j] == next_dol and temp_panel[i + 4][j] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j)
                            elif temp_panel[i - 2][j] == 0 and temp_panel[i + 4][j] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j)

                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j)
                    elif temp_panel[i - 1][j] == next_dol and temp_panel[i + 3][j] == oppo and i < 11:  # 4
                        if temp[i + 4][j] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j)
                    elif temp_panel[i - 1][j] == oppo and temp_panel[i + 3][j] == next_dol and i > 1:  # 4
                        if temp[i - 2][j] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 2][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 2) * 15 + j)
                elif i == 0:  # top
                    if temp_panel[i + 3][j] == oppo and temp_panel[i + 4][j] == 0:  # 4
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j)
                elif i == 12:  # bottom
                    if temp_panel[i - 1][j] == oppo and temp_panel[i - 2][j] == 0:  # 4
                        temp = copy.deepcopy(current_panel)
                        temp[i - 2][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 2) * 15 + j)
    # diagonal1
    for i in range(0, 12):
        for j in range(0, 12):
            if temp_panel[i][j] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][j + 2] == oppo:
                if i == 0 and j < 11:
                    if temp_panel[i + 3][j + 3] == oppo and temp_panel[i + 4][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j + 4] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j + 4)
                elif j == 0 and i < 11:
                    if temp_panel[i + 3][j + 3] == oppo and temp_panel[i + 4][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j + 4] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j + 4)
                elif 1 < i < 11 and 1 < j < 11:
                    if temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 3][j + 3] == 0:  # both empty
                        if temp_panel[i - 2][j - 2] == 0 and temp_panel[i + 4][j + 4] == next_dol:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j - 1)
                        elif temp_panel[i - 2][j - 2] == next_dol and temp_panel[i + 4][j + 4] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j + 3)
                        elif temp_panel[i - 2][j - 2] == 0 and temp_panel[i + 4][j + 4] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j - 1)

                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j + 3)
                    elif temp_panel[i - 1][j - 1] == next_dol and temp_panel[i + 3][j + 3] == oppo and \
                                    temp_panel[i + 4][j + 4] == 0:  # 4
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j + 4] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j + 4)
                    elif temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 3][j + 3] == oppo and temp_panel[i + 4][
                                j + 4] == next_dol:  # 4
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j - 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j - 1)
                elif (i == 1 and 0 < j < 11) or (j == 1 and 1 < i < 11):
                    if temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 3][j + 3] == 0:  # both empty
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j + 3)
                elif i == 11 and j < 12:
                    if temp_panel[i + 3][j + 3] == oppo and temp_panel[i - 1][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j - 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j - 1)
                elif j == 11 and i < 11:
                    if temp_panel[i + 3][j + 3] == oppo and temp_panel[i - 1][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j - 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j - 1)

    # diagonal2
    for i in range(0, 12):
        for j in range(0, 12):
            if temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][j] == oppo:
                if i == 0 and 1 < j < 11:
                    if temp_panel[i + 3][j - 1] == oppo and temp_panel[i + 4][j - 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j - 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j - 2)
                elif j == 0 and 1 < i < 11:
                    if temp_panel[i - 1][j + 3] == oppo and temp_panel[i - 2][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 2][j + 4] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 2) * 15 + j + 4)
                elif i == 1 and j == 1:
                    if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:  # both empty
                        if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == oppo:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)
                        elif temp_panel[i + 3][j - 1] == oppo and temp_panel[i - 1][j + 3] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)
                        else:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)

                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)
                elif 1 < i < 11 and 1 < j < 11:
                    if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:  # both empty
                        if temp_panel[i + 4][j - 2] == 0 and temp_panel[i - 2][j + 4] == next_dol:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)
                        elif temp_panel[i + 4][j - 2] == next_dol and temp_panel[i - 2][j + 4] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)
                        elif temp_panel[i + 4][j - 2] == 0 and temp_panel[i - 2][j + 4] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)

                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)
                    elif temp_panel[i - 1][j + 3] == oppo:
                        if temp_panel[i + 3][j - 1] == next_dol and temp_panel[i - 2][j + 4] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i - 2][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 2) * 15 + j + 4)
                        elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 2][j + 4] == next_dol:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)
                elif i == 11 and 0 < j < 11:
                    if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j + 3)
                    elif temp_panel[i + 3][j - 1] == oppo and temp_panel[i - 1][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j + 3)
                    elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == oppo and temp_panel[i - 2][
                                j + 4] == next_dol:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j - 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j - 1)
                    elif temp_panel[i + 3][j - 1] == next_dol and temp_panel[i - 1][j + 3] == oppo and \
                                    temp_panel[i - 2][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 2][j + 4] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 2) * 15 + j + 4)
                elif j == 11 and 0 < i < 11:
                    if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j - 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j - 1)
                    elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == oppo:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j - 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j - 1)
                elif i == 11 and j == 11:
                    if temp_panel[i + 3][j - 1] == oppo and temp_panel[i - 1][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j + 3)
                    elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == oppo:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j - 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j - 1)
                    elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j - 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j - 1)

                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j + 3)

    if pos != []:
        return np.array(full_mat), np.array(pos)
    # priority 3
    # to prevent 3-3
    # xoo   oxo   oox
    # o      o      o
    # o      o      o
    for i in range(0, 13):
        for j in range(0, 13):
            if temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j] == oppo and \
                            temp_panel[i + 2][j] == oppo:
                if temp_panel[i][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
            if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j + 1] == oppo and \
                            temp_panel[i + 2][j + 1] == oppo:
                if temp_panel[i][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 1] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 1)
            if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i + 1][j + 2] == oppo and \
                            temp_panel[i + 2][j + 2] == oppo:
                if temp_panel[i][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 2] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 2)
    # o      o      o
    # xoo   oxo   oox
    # o      o      o
    for i in range(1, 14):
        for j in range(0, 13):
            if temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j] == oppo and \
                            temp_panel[i - 1][j] == oppo:
                if temp_panel[i][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
            if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j + 1] == oppo and \
                            temp_panel[i - 1][j + 1] == oppo:
                if temp_panel[i][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 1] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 1)
            if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i + 1][j + 2] == oppo and \
                            temp_panel[i - 1][j + 2] == oppo:
                if temp_panel[i][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 2] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 2)
    # o      o      o
    # o      o      o
    # xoo   oxo   oox
    for i in range(2, 15):
        for j in range(0, 13):
            if temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i - 2][j] == oppo and \
                            temp_panel[i - 1][j] == oppo:
                if temp_panel[i][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
            if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i - 2][j + 1] == oppo and \
                            temp_panel[i - 1][j + 1] == oppo:
                if temp_panel[i][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 1] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 1)
            if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i - 2][j + 2] == oppo and \
                            temp_panel[i - 1][j + 2] == oppo:
                if temp_panel[i][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 2] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 2)

    # diagonal 1
    for i in range(2, 13):
        for j in range(0, 13):
            if temp_panel[i][j] == 0 and temp_panel[i - 1][j + 1] == oppo and temp_panel[i + 1][j + 1] == oppo and \
                            temp_panel[i - 2][j + 2] == oppo and temp_panel[i + 2][j + 2] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)
    # diagonal 2
    for i in range(1, 13):
        for j in range(1, 13):
            if temp_panel[i][j] == 0 and temp_panel[i - 1][j + 1] == oppo and temp_panel[i + 1][j - 1] == oppo and \
                            temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][j + 2] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)
    # diagonal 3
    for i in range(0, 13):
        for j in range(2, 13):
            if temp_panel[i][j] == 0 and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 1][j - 1] == oppo and \
                            temp_panel[i + 2][j + 2] == oppo and temp_panel[i + 2][j - 2] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)
    # diagonal 4
    for i in range(2, 14):
        for j in range(1, 13):
            if temp_panel[i][j] == 0 and temp_panel[i + 1][j + 1] == oppo and temp_panel[i - 1][
                        j - 1] == oppo and \
                            temp_panel[i - 1][j + 1] == oppo and temp_panel[i - 2][j + 2] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)
    # diagonal 5
    for i in range(1, 14):
        for j in range(1, 14):
            if temp_panel[i][j] == 0 and temp_panel[i + 1][j + 1] == oppo and temp_panel[i - 1][
                        j - 1] == oppo and \
                            temp_panel[i - 1][j + 1] == oppo and temp_panel[i + 1][j - 1] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)
    # diagonal 6
    for i in range(1, 13):
        for j in range(2, 14):
            if temp_panel[i][j] == 0 and temp_panel[i + 1][j + 1] == oppo and temp_panel[i - 1][
                        j - 1] == oppo and \
                            temp_panel[i + 2][j - 2] == oppo and temp_panel[i + 1][j - 1] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)
    # diagonal 7
    for i in range(2, 15):
        for j in range(2, 13):
            if temp_panel[i][j] == 0 and temp_panel[i - 2][j - 2] == oppo and temp_panel[i - 1][
                        j - 1] == oppo and \
                            temp_panel[i - 1][j + 1] == oppo and temp_panel[i - 2][j + 2] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)
    # diagonal 8
    for i in range(2, 14):
        for j in range(2, 14):
            if temp_panel[i][j] == 0 and temp_panel[i - 2][j - 2] == oppo and temp_panel[i - 1][
                        j - 1] == oppo and \
                            temp_panel[i - 1][j + 1] == oppo and temp_panel[i + 1][j - 1] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)
    # diagonal 9
    for i in range(2, 13):
        for j in range(2, 15):
            if temp_panel[i][j] == 0 and temp_panel[i - 2][j - 2] == oppo and temp_panel[i - 1][
                        j - 1] == oppo and \
                            temp_panel[i + 2][j - 2] == oppo and temp_panel[i + 1][j - 1] == oppo:
                temp = copy.deepcopy(current_panel)
                temp[i][j] = next_dol2
                full_mat.append(temp)
                pos.append(i * 15 + j)

    if pos != []:
        return np.array(full_mat), np.array(pos)
    else:
        return count_all(current_panel)

def count_all(current_panel):
    full_mat = []
    pos = []

    for i in range(0,15):
        for j in range(0,15):
            temp = copy.deepcopy(current_panel)
            if temp[i][j] == 0:
                temp[i][j] = 1
                full_mat.append(temp)
                pos.append(i*15 + j)
    return np.array(full_mat), np.array(pos)



def find_finisher(current_panel):
    # find next position that can win the game
    temp_panel = copy.deepcopy(current_panel)
    # oppo = -1
    mine = 1
    full_mat = []
    pos = []

    # priority 1
    # width 4
    for i in range(0, 15):
        for j in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 2] == mine and \
                            temp_panel[i][j + 3] == mine:
                # left-end
                if (j==0):
                    if temp_panel[i][j+4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 4] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 4)
                # right-end
                elif (j==11):
                    if temp_panel[i][j-1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j - 1] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j - 1)
                # others
                else:
                    if temp_panel[i][j-1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j - 1] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j - 1)

                    if temp_panel[i][j+4] ==0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j +4] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j +4)
    # height 4
    for j in range(0, 15):
        for i in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 2][j] == mine and \
                            temp_panel[i + 3][j] == mine:

                # top-end
                if(i==0):
                    if temp_panel[i + 4][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j] = mine
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j)

                # bottom-end
                elif (i==11):
                    if temp_panel[i - 1][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j)

                # others
                else:
                    if temp_panel[i + 4][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j] = mine
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j)

                        if temp_panel[i - 1][j] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j] = mine
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j)
    # diagonal 4
    for i in range(0, 12):
        for j in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 2][j + 2] == mine and \
                            temp_panel[i + 3][j + 3] == mine:

                tf_check_rb = False
                tf_check_lt = False

                # left or top end
                if(i==0 or j==0):
                    tf_check_rb = True
                # right or bottom end
                elif(i==11 or j==11):
                    tf_check_lt = True
                else:
                    tf_check_lt = True
                    tf_check_rb = True


                if(tf_check_rb):
                    if temp_panel[i + 4][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j + 4] = mine
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j + 4)

                if(tf_check_lt):
                    if temp_panel[i - 1][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j - 1] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j - 1)
    for i in range(0, 12):
        for j in range(0, 12):
            if temp_panel[i][j + 3] == mine and temp_panel[i + 1][j + 2] == mine and temp_panel[i + 2][
                        j + 1] == mine and temp_panel[i + 3][j] == mine:
                tf_check_rt = False
                tf_check_lb = False

                # right or top end
                if(i==0 or j==11):
                    tf_check_lb = True
                # left or bottom end
                elif(i==11 or j==0):
                    tf_check_rt = True
                else:
                    tf_check_rt = True
                    tf_check_lb = True

                if (tf_check_rt):
                    if temp_panel[i - 1][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j + 4] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j + 4)

                if (tf_check_lb):
                    if temp_panel[i + 4][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 4][j - 1] = mine
                        full_mat.append(temp)
                        pos.append((i + 4) * 15 + j - 1)

    # width 2-2, 3-1, 1-3
    for i in range(0, 15):
        for j in range(0, 11):
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 3] == mine and \
                            temp_panel[i][j + 4] == mine:
                if temp_panel[i][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 2] = mine
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 2)
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 2] == mine and \
                            temp_panel[i][j + 4] == mine:
                if temp_panel[i][j + 3] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 3] = mine
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 3)
            if temp_panel[i][j] == mine and temp_panel[i][j + 2] == mine and temp_panel[i][j + 3] == mine and \
                            temp_panel[i][j + 4] == mine:
                if temp_panel[i][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j + 1] = mine
                    full_mat.append(temp)
                    pos.append(i * 15 + j + 1)
    # height 2-2, 3-1, 1-3
    for j in range(0, 15):
        for i in range(0, 11):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 3][j] == mine and \
                            temp_panel[i + 4][j] == mine:
                if temp_panel[i + 2][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j] = mine
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j)
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 2][j] == mine and \
                            temp_panel[i + 4][j] == mine:
                if temp_panel[i + 3][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 3][j] = mine
                    full_mat.append(temp)
                    pos.append((i + 3) * 15 + j)
            if temp_panel[i][j] == mine and temp_panel[i + 2][j] == mine and temp_panel[i + 3][j] == mine and \
                            temp_panel[i + 4][j] == mine:
                if temp_panel[i + 1][j] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j] = mine
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j)
    # diagonal
    for i in range(0, 11):
        for j in range(0, 11):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 2][j + 2] == mine and \
                            temp_panel[i + 4][j + 4] == mine:
                if temp_panel[i + 3][j + 3] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 3][j + 3] = mine
                    full_mat.append(temp)
                    pos.append((i + 3) * 15 + j + 3)
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 3][
                        j + 3] == mine and temp_panel[i + 4][j + 4] == mine:
                if temp_panel[i + 2][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j + 2] = mine
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j + 2)
            if temp_panel[i][j] == mine and temp_panel[i + 2][j + 2] == mine and temp_panel[i + 3][
                        j + 3] == mine and temp_panel[i + 4][j + 4] == mine:
                if temp_panel[i + 1][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j + 1] = mine
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j + 1)
    for i in range(0, 11):
        for j in range(0, 11):
            if temp_panel[i][j + 4] == mine and temp_panel[i + 1][j + 3] == mine and temp_panel[i + 2][
                        j + 2] == mine and temp_panel[i + 4][j] == mine:
                if temp_panel[i + 3][j + 1] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 3][j + 1] = mine
                    full_mat.append(temp)
                    pos.append((i + 3) * 15 + j + 1)
            if temp_panel[i][j + 4] == mine and temp_panel[i + 1][j + 3] == mine and temp_panel[i + 3][
                        j + 1] == mine and temp_panel[i + 4][j] == mine:
                if temp_panel[i + 2][j + 2] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 2][j + 2] = mine
                    full_mat.append(temp)
                    pos.append((i + 2) * 15 + j + 2)
            if temp_panel[i][j + 4] == mine and temp_panel[i + 2][j + 2] == mine and temp_panel[i + 3][
                        j + 1] == mine and temp_panel[i + 4][j] == mine:
                if temp_panel[i + 1][j + 3] == 0:
                    temp = copy.deepcopy(current_panel)
                    temp[i + 1][j + 3] = mine
                    full_mat.append(temp)
                    pos.append((i + 1) * 15 + j + 3)

    if pos != []:
        return np.array(full_mat), np.array(pos)

    # priority 2
    # width xooxox or xoxoox
    for i in range(0, 15):
        for j in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 3] == mine:
                # check if both sides are playable
                # empty or not deadend
                if (j>0 and j<11):
                    if (temp_panel[i][j-1]==0 and temp_panel[i][j+4] == 0):
                        if temp_panel[i][j + 2] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 2] = mine
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 2)

            if temp_panel[i][j] == mine and temp_panel[i][j + 2] == mine and temp_panel[i][j + 3] == mine:
                # check if both sides are playable
                # empty or not deadend
                if (j>0 and j<11):
                    if (temp_panel[i][j-1]==0 and temp_panel[i][j+4] == 0):
                        if temp_panel[i][j + 1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 1] = mine
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 1)
    # height xooxox or xoxoox
    for j in range(0, 15):
        for i in range(0, 12):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 3][j] == mine:
                if (i>0 and i<11):
                    if (temp_panel[i-1][j]==0 and temp_panel[i+4][j] == 0):
                        if temp_panel[i + 2][j] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 2][j] = mine
                            full_mat.append(temp)
                            pos.append((i + 2) * 15 + j)
            if temp_panel[i][j] == mine and temp_panel[i + 2][j] == mine and temp_panel[i + 3][j] == mine:
                if (i>0 and i<11):
                    if (temp_panel[i-1][j]==0 and temp_panel[i+4][j] == 0):
                        if temp_panel[i + 1][j] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 1][j] = mine
                            full_mat.append(temp)
                            pos.append((i + 1) * 15 + j)
    # diagonal
    for i in range(0, 12):
        for j in range(0, 12):
            # need to change
            if temp_panel[i][j] == mine and temp_panel[i + 1][j + 1] == mine and temp_panel[i + 3][j + 3] == mine:
                # [i-1][j-1] and [i+4][j+4] considered
                if(i>0 and i<11) and (j>0 and j<11):
                    if(temp_panel[i-1][j-1]==0 and temp_panel[i+4][j+4]==0):
                        if temp_panel[i + 2][j + 2] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 2][j + 2] = mine
                            full_mat.append(temp)
                            pos.append((i + 2) * 15 + j + 2)
            if temp_panel[i][j] == mine and temp_panel[i + 2][j + 2] == mine and temp_panel[i + 3][j + 3] == mine:
                # [i-1][j-1] and [i+4][j+4] considered
                if(i>0 and i<11) and (j>0 and j<11):
                    if(temp_panel[i-1][j-1]==0 and temp_panel[i+4][j+4]==0):
                        if temp_panel[i + 1][j + 1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 1][j + 1] = mine
                            full_mat.append(temp)
                            pos.append((i + 1) * 15 + j + 1)
    for i in range(0, 12):
        for j in range(0, 12):
            if temp_panel[i + 3][j] == mine and temp_panel[i + 2][j + 1] == mine and temp_panel[i][j + 3] == mine:
                # [i-1][j+4] and [i+4][j-1] considered
                if(i>0 and i<11) and (j>0 and j<11):
                    if(temp_panel[i-1][j+4]==0 and temp_panel[i+4][j-1]==0):
                        if temp_panel[i + 1][j + 2] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 1][j + 2] = mine
                            full_mat.append(temp)
                            pos.append((i + 1) * 15 + j + 2)
            if temp_panel[i + 3][j] == mine and temp_panel[i + 1][j + 2] == mine and temp_panel[i][j + 3] == mine:
                # [i-1][j+4] and [i+4][j-1] considered
                if(i>0 and i<11) and (j>0 and j<11):
                    if(temp_panel[i-1][j+4]==0 and temp_panel[i+4][j-1]==0):
                        if temp_panel[i + 2][j + 1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 2][j + 1] = mine
                            full_mat.append(temp)
                            pos.append((i + 2) * 15 + j + 1)
    # width 3
    # need to change
    for i in range(0, 15):
        for j in range(1, 12):
            if temp_panel[i][j] == mine and temp_panel[i][j + 1] == mine and temp_panel[i][j + 2] == mine:

                # neighbor places should be empty
                if temp_panel[i][j - 1] == 0 and temp_panel[i][j + 3] == 0:  # xooox
                    # check whether blocked
                    # if j==1 --> it must be j+3
                    # if j==11 --> it must be j-1
                    tf_r_block = False
                    tf_l_block = False

                    if(j==1):
                        tf_l_block = True
                    elif(j==11):
                        tf_r_block = True

                    try:
                        if(temp_panel[i][j - 2]==-1):
                            tf_l_block = True
                    except:
                        pass

                    try:
                        if(temp_panel[i][j + 4]==-1):
                            tf_r_block = True
                    except:
                        pass

                    if (not tf_r_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 3] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 3)

                    if (not tf_l_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i][j - 1] = mine
                        full_mat.append(temp)
                        pos.append(i * 15 + j - 1)

    # height over 3
    for j in range(0, 15):
        for i in range(1, 12):
            if temp_panel[i][j] == mine and temp_panel[i + 1][j] == mine and temp_panel[i + 2][j] == mine:
                # neighbor places should be empty
                if temp_panel[i-1][j] == 0 and temp_panel[i + 3][j] == 0:  # xooox
                    # check whether blocked
                    # if i==1 --> it must be i+3
                    # if i==11 --> it must be i-1
                    tf_b_block = False
                    tf_t_block = False

                    if(i == 1):
                        tf_t_block = True
                    elif (i == 11):
                        tf_b_block = True

                    try:
                        if (temp_panel[i-2][j] == -1):
                            tf_t_block = True
                    except:
                        pass

                    try:
                        if (temp_panel[i+4][j] == -1):
                            tf_b_block = True
                    except:
                        pass


                    if (not tf_b_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j] = mine
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j)

                    if (not tf_t_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j)

    # diagonal1
    for j in range(1, 12):
        for i in range(1, 12):
            # exclude edges
            if temp_panel[i][j] == mine and temp_panel[i + 1][j+1] == mine and temp_panel[i + 2][j+2] == mine:
                if temp_panel[i+3][j + 3] == 0 and temp_panel[i - 1][j - 1] == 0:  # xooox

                    tf_rb_block = False
                    tf_lt_block = False

                    # left or top
                    if (i == 1 or j == 1):
                        tf_lt_block = True
                    # right or bottom
                    elif (i == 11 or j == 11):
                        tf_rb_block = True

                    try:
                        if (temp_panel[i - 2][j - 2] == -1):
                            tf_lt_block = True
                    except:
                        pass
                    try:
                        if (temp_panel[i + 4][j + 4] == -1):
                            tf_rb_block = True
                    except:
                        pass

                    if(not tf_rb_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j + 3] = mine
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j + 3)

                    if(not tf_lt_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j - 1] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j - 1)
    # diagonal2
    for j in range(1, 12):
        for i in range(1, 12):
            # exclude edges
            if temp_panel[i+2][j] == mine and temp_panel[i + 1][j+1] == mine and temp_panel[i][j+2] == mine:
                if temp_panel[i+3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:  # xooox
                    tf_rt_block = False
                    tf_lb_block = False

                    # right or top end
                    if (i == 1 or j == 11):
                        tf_rt_block = True
                    # left or bottom end
                    elif (i == 11 or j == 1):
                        tf_lb_block = True

                    try:
                        if(temp_panel[i+4][j - 2] == -1):
                            tf_lb_block = True
                    except:
                        pass
                    try:
                        if(temp_panel[i-2][j + 4] == -1):
                            tf_rt_block = True
                    except:
                        pass

                    if (not tf_lb_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j - 1] = mine
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j - 1)

                    if (not tf_rt_block):
                        temp = copy.deepcopy(current_panel)
                        temp[i - 1][j + 3] = mine
                        full_mat.append(temp)
                        pos.append((i - 1) * 15 + j + 3)

    if pos != []:
        return np.array(full_mat), np.array(pos)

    # error occurs if there is no available finisher

def get_available_counts(current_panel, color):
    full_mat = []
    pos = []
    next_dol = 0
    if color == 1:
        next_dol = 1
        next_dol2 = 1
        oppo = -1
    elif color == -1:
        next_dol = -1
        oppo = 1
    temp_panel = copy.deepcopy(current_panel)

    if next_dol == 1:
        # have to defense
        # priority 1

        # width 2-2, 3-1, 1-3
        for i in range(0, 15):
            for j in range(0, 11):
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 3] == oppo and \
                                temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and \
                                temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 3)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i][j + 3] == oppo and \
                                temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
        # height 2-2, 3-1, 1-3
        for j in range(0, 15):
            for i in range(0, 11):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 3][j] == oppo and \
                                temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 2][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 2][j] == oppo and \
                                temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 3][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i + 2][j] == oppo and temp_panel[i + 3][j] == oppo and \
                                temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 1][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j)
        # diagonal
        for i in range(0, 11):
            for j in range(0, 11):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][
                            j + 2] == oppo and temp_panel[i + 4][j + 4] == oppo:
                    if temp_panel[i + 3][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j + 3)
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 3][
                            j + 3] == oppo and temp_panel[i + 4][j + 4] == oppo:
                    if temp_panel[i + 2][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i + 2][j + 2] == oppo and temp_panel[i + 3][
                            j + 3] == oppo and temp_panel[i + 4][j + 4] == oppo:
                    if temp_panel[i + 1][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j + 1)
        for i in range(0, 11):
            for j in range(0, 11):
                if temp_panel[i][j + 4] == oppo and temp_panel[i + 1][j + 3] == oppo and temp_panel[i + 2][
                            j + 2] == oppo and temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 3][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j + 1)
                if temp_panel[i][j + 4] == oppo and temp_panel[i + 1][j + 3] == oppo and temp_panel[i + 3][
                            j + 1] == oppo and temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 2][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j + 2)
                if temp_panel[i][j + 4] == oppo and temp_panel[i + 2][j + 2] == oppo and temp_panel[i + 3][
                            j + 1] == oppo and temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 1][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j + 3)

        if pos != []:
            return np.array(full_mat), np.array(pos)

        # priority 2
        # width xooxox or xoxoox
        for i in range(0, 15):
            for j in range(1, 11):
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 3] == oppo and \
                                temp_panel[i][j + 2] == 0:
                    if temp_panel[i][j + 4] == 0 and temp_panel[i][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i][j + 3] == oppo and \
                                temp_panel[i][j + 1] == 0:
                    if temp_panel[i][j + 4] == 0 and temp_panel[i][j - 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
        # height xooxox or xoxoox
        for j in range(0, 15):
            for i in range(1, 11):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 3][j] == oppo and \
                                temp_panel[i + 2][j] == 0:
                    if temp_panel[i + 4][j] == 0 and temp_panel[i - 1][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i + 2][j] == oppo and temp_panel[i + 3][j] == oppo and \
                                temp_panel[i + 1][j] == 0:
                    if temp_panel[i + 4][j] == 0 and temp_panel[i - 1][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j)
        # diagonal
        for i in range(1, 11):
            for j in range(1, 12):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 3][
                            j + 3] == oppo and temp_panel[i + 2][j + 2] == 0:
                    if temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 4][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i + 2][j + 2] == oppo and temp_panel[i + 3][
                            j + 3] == oppo and temp_panel[i + 1][j + 1] == 0:
                    if temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 4][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j + 1)
        for i in range(1, 11):
            for j in range(1, 11):
                if temp_panel[i + 3][j] == oppo and temp_panel[i + 2][j + 1] == oppo and temp_panel[i][
                            j + 3] == oppo and temp_panel[i + 1][j + 2] == 0:
                    if temp_panel[i + 4][j - 1] == 0 and temp_panel[i - 1][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j + 2)
                if temp_panel[i + 3][j] == oppo and temp_panel[i + 1][j + 2] == oppo and temp_panel[i][
                            j + 3] == oppo and temp_panel[i + 2][j + 1] == 0:
                    if temp_panel[i + 4][j - 1] == 0 and temp_panel[i - 1][j + 4] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j + 1)

        # width over 3
        for i in range(0, 15):
            for j in range(0, 13):
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo:
                    if 12 > j > 0:
                        if temp_panel[i][j - 1] == 0 and temp_panel[i][j + 3] == 0:  # xooox
                            if j == 1:
                                temp = copy.deepcopy(current_panel)
                                temp[i][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append(i * 15 + j + 3)
                            elif j == 11:
                                temp = copy.deepcopy(current_panel)
                                temp[i][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append(i * 15 + j - 1)
                            elif 1 < j < 11:
                                if temp_panel[i][j - 2] == 0 and temp_panel[i][j + 4] == next_dol:
                                    temp = copy.deepcopy(current_panel)
                                    temp[i][j - 1] = next_dol2
                                    full_mat.append(temp)
                                    pos.append(i * 15 + j - 1)
                                elif temp_panel[i][j - 2] == next_dol and temp_panel[i][j + 4] == 0:
                                    temp = copy.deepcopy(current_panel)
                                    temp[i][j + 3] = next_dol2
                                    full_mat.append(temp)
                                    pos.append(i * 15 + j + 3)
                                elif temp_panel[i][j - 2] == 0 and temp_panel[i][j + 4] == 0:
                                    temp = copy.deepcopy(current_panel)
                                    temp[i][j - 1] = next_dol2
                                    full_mat.append(temp)
                                    pos.append(i * 15 + j - 1)

                                    temp = copy.deepcopy(current_panel)
                                    temp[i][j + 3] = next_dol2
                                    full_mat.append(temp)
                                    pos.append(i * 15 + j + 3)

                        elif temp_panel[i][j - 1] == next_dol and temp_panel[i][j + 3] == oppo and j < 11:
                            if temp_panel[i][j + 4] == 0:  # Moooox
                                temp = copy.deepcopy(current_panel)
                                temp[i][j + 4] = next_dol2
                                full_mat.append(temp)
                                pos.append(i * 15 + j + 4)

                        elif temp_panel[i][j - 1] == oppo and temp_panel[i][j + 3] == next_dol and j > 2:
                            if temp_panel[i][j - 2] == 0:  # xooooM
                                temp = copy.deepcopy(current_panel)
                                temp[i][j - 2] = next_dol2
                                full_mat.append(temp)
                                pos.append(i * 15 + j - 2)
                    elif j == 0:  # left end
                        if temp_panel[i][j + 3] == oppo and temp_panel[i][j + 4] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 4)
                    elif j == 12:  # right end
                        if temp_panel[i][j - 1] == oppo and temp_panel[i][j - 2] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i][j - 2] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 2)
        # height over 3
        for j in range(0, 15):
            for i in range(0, 13):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 2][j] == oppo:
                    if 12 > i > 0:
                        if temp_panel[i - 1][j] == 0 and temp_panel[i + 3][j] == 0:  # both empty
                            if i == 1:
                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j)
                            elif i == 11:
                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j)
                            elif 1 < i < 11:
                                if temp_panel[i - 2][j] == 0 and temp_panel[i + 4][j] == next_dol:
                                    temp = copy.deepcopy(current_panel)
                                    temp[i - 1][j] = next_dol2
                                    full_mat.append(temp)
                                    pos.append((i - 1) * 15 + j)
                                elif temp_panel[i - 2][j] == next_dol and temp_panel[i + 4][j] == 0:
                                    temp = copy.deepcopy(current_panel)
                                    temp[i + 3][j] = next_dol2
                                    full_mat.append(temp)
                                    pos.append((i + 3) * 15 + j)
                                elif temp_panel[i - 2][j] == 0 and temp_panel[i + 4][j] == 0:
                                    temp = copy.deepcopy(current_panel)
                                    temp[i - 1][j] = next_dol2
                                    full_mat.append(temp)
                                    pos.append((i - 1) * 15 + j)

                                    temp = copy.deepcopy(current_panel)
                                    temp[i + 3][j] = next_dol2
                                    full_mat.append(temp)
                                    pos.append((i + 3) * 15 + j)
                        elif temp_panel[i - 1][j] == next_dol and temp_panel[i + 3][j] == oppo and i < 11:  # 4
                            if temp[i + 4][j] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i + 4][j] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 4) * 15 + j)
                        elif temp_panel[i - 1][j] == oppo and temp_panel[i + 3][j] == next_dol and i > 1:  # 4
                            if temp[i - 2][j] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i - 2][j] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 2) * 15 + j)
                    elif i == 0:  # top
                        if temp_panel[i + 3][j] == oppo and temp_panel[i + 4][j] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j)
                    elif i == 12:  # bottom
                        if temp_panel[i - 1][j] == oppo and temp_panel[i - 2][j] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i - 2][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 2) * 15 + j)
        # diagonal1
        for i in range(0, 12):
            for j in range(0, 12):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][j + 2] == oppo:
                    if i == 0 and j < 11:
                        if temp_panel[i + 3][j + 3] == oppo and temp_panel[i + 4][j + 4] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j + 4)
                    elif j == 0 and i < 11:
                        if temp_panel[i + 3][j + 3] == oppo and temp_panel[i + 4][j + 4] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j + 4)
                    elif 1 < i < 11 and 1 < j < 11:
                        if temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 3][j + 3] == 0:  # both empty
                            if temp_panel[i - 2][j - 2] == 0 and temp_panel[i + 4][j + 4] == next_dol:
                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j - 1)
                            elif temp_panel[i - 2][j - 2] == next_dol and temp_panel[i + 4][j + 4] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j + 3)
                            elif temp_panel[i - 2][j - 2] == 0 and temp_panel[i + 4][j + 4] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j - 1)

                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j + 3)
                        elif temp_panel[i - 1][j - 1] == next_dol and temp_panel[i + 3][j + 3] == oppo and \
                                        temp_panel[i + 4][j + 4] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j + 4)
                        elif temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 3][j + 3] == oppo and temp_panel[i + 4][
                                    j + 4] == next_dol:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j - 1)
                    elif (i == 1 and 0 < j < 11) or (j == 1 and 1 < i < 11):
                        if temp_panel[i - 1][j - 1] == 0 and temp_panel[i + 3][j + 3] == 0:  # both empty
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j + 3)
                    elif i == 11 and j < 12:
                        if temp_panel[i + 3][j + 3] == oppo and temp_panel[i - 1][j - 1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j - 1)
                    elif j == 11 and i < 11:
                        if temp_panel[i + 3][j + 3] == oppo and temp_panel[i - 1][j - 1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j - 1)

        # diagonal2
        for i in range(0, 12):
            for j in range(0, 12):
                if temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][j] == oppo:
                    if i == 0 and 1 < j < 11:
                        if temp_panel[i + 3][j - 1] == oppo and temp_panel[i + 4][j - 2] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j - 2] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j - 2)
                    elif j == 0 and 1 < i < 11:
                        if temp_panel[i - 1][j + 3] == oppo and temp_panel[i - 2][j + 4] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 2][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 2) * 15 + j + 4)
                    elif i == 1 and j == 1:
                        if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:  # both empty
                            if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == oppo:
                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j - 1)
                            elif temp_panel[i + 3][j - 1] == oppo and temp_panel[i - 1][j + 3] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j + 3)
                            else:
                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j - 1)

                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j + 3)
                    elif 1 < i < 11 and 1 < j < 11:
                        if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:  # both empty
                            if temp_panel[i + 4][j - 2] == 0 and temp_panel[i - 2][j + 4] == next_dol:
                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j - 1)
                            elif temp_panel[i + 4][j - 2] == next_dol and temp_panel[i - 2][j + 4] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j + 3)
                            elif temp_panel[i + 4][j - 2] == 0 and temp_panel[i - 2][j + 4] == 0:
                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j - 1)

                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j + 3)
                        elif temp_panel[i - 1][j + 3] == oppo:
                            if temp_panel[i + 3][j - 1] == next_dol and temp_panel[i - 2][j + 4] == 0:  # 4
                                temp = copy.deepcopy(current_panel)
                                temp[i - 2][j + 4] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 2) * 15 + j + 4)
                            elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 2][j + 4] == next_dol:  # 4
                                temp = copy.deepcopy(current_panel)
                                temp[i + 3][j - 1] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 3) * 15 + j - 1)
                    elif i == 11 and 0 < j < 11:
                        if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)
                        elif temp_panel[i + 3][j - 1] == oppo and temp_panel[i - 1][j + 3] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)
                        elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == oppo and temp_panel[i - 2][
                                    j + 4] == next_dol:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)
                        elif temp_panel[i + 3][j - 1] == next_dol and temp_panel[i - 1][j + 3] == oppo and \
                                        temp_panel[i - 2][j + 4] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 2][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 2) * 15 + j + 4)
                    elif j == 11 and 0 < i < 11:
                        if temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)
                        elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == oppo:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)
                    elif i == 11 and j == 11:
                        if temp_panel[i + 3][j - 1] == oppo and temp_panel[i - 1][j + 3] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)
                        elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == oppo:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)
                        elif temp_panel[i + 3][j - 1] == 0 and temp_panel[i - 1][j + 3] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j - 1)

                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)

        if pos != []:
            return np.array(full_mat), np.array(pos)
        # priority 3
        # to prevent 3-3
        # xoo   oxo   oox
        # o      o      o
        # o      o      o
        for i in range(0, 13):
            for j in range(0, 13):
                if temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j] == oppo and \
                                temp_panel[i + 2][j] == oppo:
                    if temp_panel[i][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j + 1] == oppo and \
                                temp_panel[i + 2][j + 1] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i + 1][j + 2] == oppo and \
                                temp_panel[i + 2][j + 2] == oppo:
                    if temp_panel[i][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)
        # o      o      o
        # xoo   oxo   oox
        # o      o      o
        for i in range(1, 14):
            for j in range(0, 13):
                if temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j] == oppo and \
                                temp_panel[i - 1][j] == oppo:
                    if temp_panel[i][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j + 1] == oppo and \
                                temp_panel[i - 1][j + 1] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i + 1][j + 2] == oppo and \
                                temp_panel[i - 1][j + 2] == oppo:
                    if temp_panel[i][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)
        # o      o      o
        # o      o      o
        # xoo   oxo   oox
        for i in range(2, 15):
            for j in range(0, 13):
                if temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i - 2][j] == oppo and \
                                temp_panel[i - 1][j] == oppo:
                    if temp_panel[i][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i - 2][j + 1] == oppo and \
                                temp_panel[i - 1][j + 1] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i - 2][j + 2] == oppo and \
                                temp_panel[i - 1][j + 2] == oppo:
                    if temp_panel[i][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)

        # diagonal 1
        for i in range(2, 13):
            for j in range(0, 13):
                if temp_panel[i][j] == 0 and temp_panel[i - 1][j + 1] == oppo and temp_panel[i + 1][j + 1] == oppo and \
                                temp_panel[i - 2][j + 2] == oppo and temp_panel[i + 2][j + 2] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
        # diagonal 2
        for i in range(1, 13):
            for j in range(1, 13):
                if temp_panel[i][j] == 0 and temp_panel[i - 1][j + 1] == oppo and temp_panel[i + 1][j - 1] == oppo and \
                                temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][j + 2] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
        # diagonal 3
        for i in range(0, 13):
            for j in range(2, 13):
                if temp_panel[i][j] == 0 and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 1][j - 1] == oppo and \
                                temp_panel[i + 2][j + 2] == oppo and temp_panel[i + 2][j - 2] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
        # diagonal 4
        for i in range(2, 14):
            for j in range(1, 13):
                if temp_panel[i][j] == 0 and temp_panel[i + 1][j + 1] == oppo and temp_panel[i - 1][
                            j - 1] == oppo and \
                                temp_panel[i - 1][j + 1] == oppo and temp_panel[i - 2][j + 2] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
        # diagonal 5
        for i in range(1, 14):
            for j in range(1, 14):
                if temp_panel[i][j] == 0 and temp_panel[i + 1][j + 1] == oppo and temp_panel[i - 1][
                            j - 1] == oppo and \
                                temp_panel[i - 1][j + 1] == oppo and temp_panel[i + 1][j - 1] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
        # diagonal 6
        for i in range(1, 13):
            for j in range(2, 14):
                if temp_panel[i][j] == 0 and temp_panel[i + 1][j + 1] == oppo and temp_panel[i - 1][
                            j - 1] == oppo and \
                                temp_panel[i + 2][j - 2] == oppo and temp_panel[i + 1][j - 1] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
        # diagonal 7
        for i in range(2, 15):
            for j in range(2, 13):
                if temp_panel[i][j] == 0 and temp_panel[i - 2][j - 2] == oppo and temp_panel[i - 1][
                            j - 1] == oppo and \
                                temp_panel[i - 1][j + 1] == oppo and temp_panel[i - 2][j + 2] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
        # diagonal 8
        for i in range(2, 14):
            for j in range(2, 14):
                if temp_panel[i][j] == 0 and temp_panel[i - 2][j - 2] == oppo and temp_panel[i - 1][
                            j - 1] == oppo and \
                                temp_panel[i - 1][j + 1] == oppo and temp_panel[i + 1][j - 1] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)
        # diagonal 9
        for i in range(2, 13):
            for j in range(2, 15):
                if temp_panel[i][j] == 0 and temp_panel[i - 2][j - 2] == oppo and temp_panel[i - 1][
                            j - 1] == oppo and \
                                temp_panel[i + 2][j - 2] == oppo and temp_panel[i + 1][j - 1] == oppo:
                    temp = copy.deepcopy(current_panel)
                    temp[i][j] = next_dol2
                    full_mat.append(temp)
                    pos.append(i * 15 + j)

        if pos != []:
            return np.array(full_mat), np.array(pos)

        # full
        for i in range(0, 15):
            for j in range(0, 15):
                temp = copy.deepcopy(current_panel)
                if temp[i][j] == 0:
                    temp[i][j] = next_dol
                    full_mat.append(temp)
                    pos.append(i * 15 + j)

        return np.array(full_mat), np.array(pos)


if __name__ == '__main__':
    panel = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    ]

    # result1, result2 = find_finisher(panel)
    result1, result2 = get_available_counts(panel,1)

    # result = get_available_counts(panel, 1)

    # for a in range(len(result[0])):
    #     print a+1, result[1][a]
    #     print result[0][a]
    print "======"
    print result1
    print "======"
    print "======"
    print result2
    print "======"