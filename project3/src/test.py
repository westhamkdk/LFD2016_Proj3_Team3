import numpy as np
import copy


def get_available_counts(current_panel, color):
    full_mat = []
    pos = []
    next_dol = 0
    if color == 1:
        next_dol = 1
        next_dol2 = 8
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
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 3] == oppo and temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j+2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 3)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i][j + 3] == oppo and temp_panel[i][j + 4] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
        # height 2-2, 3-1, 1-3
        for j in range(0, 15):
            for i in range(0, 11):
                if temp_panel[i][j] == oppo and temp_panel[i+1][j] == oppo and temp_panel[i+3][j] == oppo and temp_panel[i+4][j] == oppo:
                    if temp_panel[i + 2][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 2][j] == oppo and temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 3][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 3][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 3) * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i + 2][j] == oppo and temp_panel[i + 3][j] == oppo and temp_panel[i + 4][j] == oppo:
                    if temp_panel[i + 1][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j)
        # diagonal
        for i in range(0, 11):
            for j in range(0, 11):
                if temp_panel[i][j] == oppo and temp_panel[i+1][j+1] == oppo and temp_panel[i+2][j+2] == oppo and temp_panel[i+4][j+4] == oppo:
                    if temp_panel[i+3][j + 3] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i+3][j + 3] = next_dol2
                        full_mat.append(temp)
                        pos.append((i+3) * 15 + j + 3)
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
                if temp_panel[i][j+4] == oppo and temp_panel[i + 1][j + 3] == oppo and temp_panel[i + 2][
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
            for j in range(0, 12):
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i][j + 3] == oppo:
                    if temp_panel[i][j+2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j+2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i][j + 3] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
        # height xooxox or xoxoox
        for j in range(0, 15):
            for i in range(0, 12):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 3][j] == oppo:
                    if temp_panel[i + 2][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i + 2][j] == oppo and temp_panel[i + 3][j] == oppo:
                    if temp_panel[i + 1][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j)
        # diagonal
        for i in range(0, 12):
            for j in range(0, 12):
                if temp_panel[i][j] == oppo and temp_panel[i+1][j + 1] == oppo and temp_panel[i+3][j + 3] == oppo:
                    if temp_panel[i+2][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i+2][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i+2) * 15 + j + 2)
                if temp_panel[i][j] == oppo and temp_panel[i+2][j + 2] == oppo and temp_panel[i+3][j + 3] == oppo:
                    if temp_panel[i+1][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i+1][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i+1) * 15 + j + 1)
        for i in range(0, 12):
            for j in range(0, 12):
                if temp_panel[i+3][j] == oppo and temp_panel[i + 2][j + 1] == oppo and temp_panel[i][j + 3] == oppo:
                    if temp_panel[i + 1][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 1][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 1) * 15 + j + 2)
                if temp_panel[i+3][j] == oppo and temp_panel[i + 1][j + 2] == oppo and temp_panel[i][j + 3] == oppo:
                    if temp_panel[i + 2][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i + 2][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append((i + 2) * 15 + j + 1)
        # width over 3
        for i in range(0, 15):
            for j in range(0, 13):
                if temp_panel[i][j] == oppo and temp_panel[i][j+1] == oppo and temp_panel[i][j + 2] == oppo:

                    if 12 > j > 0:
                        if temp_panel[i][j - 1] == 0 and temp_panel[i][j + 3] == 0:  # xooox
                            temp = copy.deepcopy(current_panel)
                            temp[i][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 1)

                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 3)

                        elif temp_panel[i][j - 1] == next_dol and temp_panel[i][j + 3] == oppo and temp[i][j+4] == 0:  # Moooox
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 4)

                        elif temp_panel[i][j - 1] == oppo and temp_panel[i][j + 3] == next_dol and temp[i][j-2] == 0:  # xooooM
                            temp = copy.deepcopy(current_panel)
                            temp[i][j-2] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 2)
                    elif j == 0:  # left end
                        if temp_panel[i][j + 3] == oppo and temp_panel[i][j+4] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 4)
                    elif j == 12:  # right end
                        if temp_panel[i][j - 1] == oppo and temp_panel[i][j-2] == 0:  # 4
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
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j)

                            temp = copy.deepcopy(current_panel)
                            temp[i+3][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i+3) * 15 + j)
                        elif temp_panel[i-1][j] == next_dol and temp_panel[i + 3][j] == oppo:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i+4][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i+4) * 15 + j)
                        elif temp_panel[i-1][j] == oppo and temp_panel[i+3][j] == next_dol:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i-2][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i-2) * 15 + j)
                    elif i == 0:  # top
                        if temp_panel[i + 3][j] == oppo and temp_panel[i+4][j] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j)
                    elif i == 12:  # bottom
                        if temp_panel[i - 1][j] == oppo and temp_panel[i-2][j] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i - 2][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 2) * 15 + j)
        # diagonal1
        for i in range(0, 12):
            for j in range(0, 12):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j+1] == oppo and temp_panel[i + 2][j+2] == oppo:
                    if 0 < i < 11 and 0 < j < 11:
                        if temp_panel[i - 1][j-1] == 0 and temp_panel[i + 3][j+3] == 0:  # both empty
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j-1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j-1)

                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j+3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j+3)
                        elif temp_panel[i - 1][j-1] == next_dol and temp_panel[i + 3][j+3] == oppo and temp_panel[i+4][j+4] == 0:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j+4] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j+4)
                        elif temp_panel[i-1][j-1] == 0 and temp_panel[i+3][j+3] == oppo and temp_panel[i+4][j+4] == next_dol:  # 4
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j-1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j-1)
                    if i == 0 and j < 11:
                        if temp_panel[i+3][j+3] == oppo and temp_panel[i+4][j+4] == 0:
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
                    if i == 11 and j < 11:
                        if temp_panel[i + 3][j + 3] == oppo and temp_panel[i-1][j-1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i-1][j-1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i-1) * 15 + j-1)
                    elif j == 11 and i < 11:
                        if temp_panel[i + 3][j + 3] == oppo and temp_panel[i-1][j-1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j - 1)
                    elif i == 11 and j == 11:
                        if temp_panel[i + 3][j + 3] == oppo and temp_panel[i-1][j-1] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i-1][j-1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i-1) * 15 + j-1)

        # diagonal2
        for i in range(0, 12):
            for j in range(0, 12):
                if temp_panel[i][j+2] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i + 2][j] == oppo:
                    if 0 < i < 12 and 0 < j < 12:
                        if temp_panel[i + 3][j - 1] == 0 and temp_panel[i-1][j + 3] == 0:  # both empty
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append((i+3) * 15 + j - 1)

                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)

                        if i > 2 and j > 2:
                            if temp_panel[i - 1][j + 3] == next_dol and temp_panel[i + 3][j - 1] == oppo and temp_panel[i + 4][j - 2] == 0:  # 4
                                temp = copy.deepcopy(current_panel)
                                temp[i + 4][j - 2] = next_dol2
                                full_mat.append(temp)
                                pos.append((i + 4) * 15 + j - 2)
                            elif temp_panel[i - 1][j + 3] == 0 and temp_panel[i + 3][j - 1] == oppo and temp_panel[i + 4][j - 2] == next_dol:  # 4
                                temp = copy.deepcopy(current_panel)
                                temp[i - 1][j + 3] = next_dol2
                                full_mat.append(temp)
                                pos.append((i - 1) * 15 + j + 3)
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
                    if i == 11 and j < 11:
                        if temp_panel[i + 3][j - 1] == oppo and temp_panel[i - 1][j + 3] == 0:
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j + 3)
                    elif j == 11 and i < 11:
                        if temp_panel[i - 1][j + 3] == oppo and temp_panel[i + 3][j - 1] == 0:
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

        if pos != []:
            return np.array(full_mat), np.array(pos)
        # priority 3
        # to prevent 3-3
        # xoo   oxo   oox
        # o      o      o
        # o      o      o
        for i in range(0, 13):
            for j in range(0, 13):
                if temp_panel[i][j+1] == oppo and temp_panel[i][j+2] == oppo and temp_panel[i+1][j] == oppo and temp_panel[i+2][j] == oppo:
                    if temp_panel[i][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j+1] == oppo and temp_panel[i + 2][j+1] == oppo:
                    if temp_panel[i][j+1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j+1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j+1)
                if temp_panel[i][j] == oppo and temp_panel[i][j+1] == oppo and temp_panel[i + 1][j+2] == oppo and temp_panel[i + 2][j+2] == oppo:
                    if temp_panel[i][j+2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j+2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j+2)
        # o      o      o
        # xoo   oxo   oox
        # o      o      o
        for i in range(1, 14):
            for j in range(0, 13):
                if temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i-1][j] == oppo:
                    if temp_panel[i][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i + 1][j + 1] == oppo and temp_panel[i-1][j + 1] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i + 1][j + 2] == oppo and temp_panel[i -1][j + 2] == oppo:
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
                if temp_panel[i][j + 1] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i-2][j] == oppo and temp_panel[i - 1][j] == oppo:
                    if temp_panel[i][j] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 2] == oppo and temp_panel[i -2][j + 1] == oppo and temp_panel[i - 1][j + 1] == oppo:
                    if temp_panel[i][j + 1] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 1] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 1)
                if temp_panel[i][j] == oppo and temp_panel[i][j + 1] == oppo and temp_panel[i -2][j + 2] == oppo and temp_panel[i - 1][j + 2] == oppo:
                    if temp_panel[i][j + 2] == 0:
                        temp = copy.deepcopy(current_panel)
                        temp[i][j + 2] = next_dol2
                        full_mat.append(temp)
                        pos.append(i * 15 + j + 2)

        # diagonal 1
        for i in range(2, 13):
            for j in range(0, 13):
                if temp_panel[i][j] == 0 and temp_panel[i-1][j+1] == oppo and temp_panel[i+1][j+1] == oppo and temp_panel[i-2][j+2] == oppo and temp_panel[i+2][j+2] == oppo:
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
        [0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    target = np.array(panel)
    print target
    print

    result = get_available_counts(panel, 1)

    for a in range(len(result[0])):
        print a+1, result[1][a]
        print result[0][a]