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

    # 내가 1인 경우
    if next_dol == 1:
        # 가로 3개 이상인 경우
        for i in range(0, 15):
            for j in range(0, 13):
                if temp_panel[i][j] == oppo and temp_panel[i][j+1] == oppo and temp_panel[i][j + 2] == oppo:

                    if 12 > j > 0:
                        if temp_panel[i][j - 1] == 0 and temp_panel[i][j + 3] == 0:  # 앞뒤가 다 비어있는 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 1)

                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 3)

                        elif temp_panel[i][j - 1] == next_dol and temp_panel[i][j + 3] == oppo:  # 앞은 막히고 뒤는 상대라 4개인 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 4)

                        elif temp_panel[i][j - 1] == oppo and temp_panel[i][j + 3] == next_dol:  # 뒤를 막고 앞이 상대라 4개 연속인 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i][j-2] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 2)
                    elif j == 0:  # 제일 왼쪽
                        if temp_panel[i][j + 3] == 0:  # 뒤가 비어있는 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 3] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 3)
                        if temp_panel[i][j + 3] == oppo and temp_panel[i][j+4] == 0:  # 상대가 4개 연속인 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i][j + 4] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j + 4)
                    elif j == 12:  # 제일 오른쪽
                        if temp_panel[i][j - 1] == 0:  # 앞이 비어있는 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i][j - 1] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 1)
                        if temp_panel[i][j - 1] == oppo and temp_panel[i][j-2] == 0:  # 상대가 4개연속인 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i][j - 2] = next_dol2
                            full_mat.append(temp)
                            pos.append(i * 15 + j - 2)
        # 세로 3개 이상인 경우
        for j in range(0, 15):
            for i in range(0, 13):
                if temp_panel[i][j] == oppo and temp_panel[i + 1][j] == oppo and temp_panel[i + 2][j] == oppo:

                    if 12 > i > 0:
                        if temp_panel[i - 1][j] == 0 and temp_panel[i + 3][j] == 0:  # 앞뒤가 다 비어있는 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j)

                            temp = copy.deepcopy(current_panel)
                            temp[i+3][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i+3) * 15 + j)
                        elif temp_panel[i-1][j] == next_dol and temp_panel[i + 3][j] == oppo:  # 앞은 막히고 뒤까지 4개 연결
                            temp = copy.deepcopy(current_panel)
                            temp[i+4][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i+4) * 15 + j)
                        elif temp_panel[i-1][j] == oppo and temp_panel[i+3][j] == next_dol:  # 뒤는 막히고 앞은 4개 연결
                            temp = copy.deepcopy(current_panel)
                            temp[i-2][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i-2) * 15 + j)
                    elif i == 0:  # 맨 위쪽
                        if temp_panel[i + 3][j] == 0:  # 아래가 비어있는 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i + 3][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 3) * 15 + j)
                        elif temp_panel[i + 3][j] == oppo and temp_panel[i+4][j] == 0:  # 4개연속
                            temp = copy.deepcopy(current_panel)
                            temp[i + 4][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i + 4) * 15 + j)
                    elif i == 12:  # 맨 아래
                        if temp_panel[i - 1][j] == 0:  # 위가 비어있는 경우
                            temp = copy.deepcopy(current_panel)
                            temp[i - 1][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 1) * 15 + j)
                        elif temp_panel[i - 1][j] == oppo and temp_panel[i-2][j] == 0:  # 4개연속
                            temp = copy.deepcopy(current_panel)
                            temp[i - 2][j] = next_dol2
                            full_mat.append(temp)
                            pos.append((i - 2) * 15 + j)

        if pos != []:
            return np.array(full_mat), np.array(pos)
        elif pos == []:
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
        [-1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 0, -1, -1, -1, -1],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 0, 0, 0, -1],
        [-1, 0, 0, 0, 0, 0, 1, -1, -1, -1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1]
    ]
    target = np.array(panel)
    print target
    print

    result = get_available_counts(panel, 1)

    for a in range(len(result[0])):
        print a+1, result[1][a]
        print result[0][a]