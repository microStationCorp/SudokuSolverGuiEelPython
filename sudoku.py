import eel
import numpy as np

eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def pyFunc(brd):
    brd = np.asarray(brd).astype(int)
    zeros = get_empty(brd)
    z = 0
    while z < len(zeros) and z >= 0:
        num = num = brd[zeros[z]] + 1
        while num < 10:
            if not check_row_column(brd[zeros[z][0]], num) and not check_row_column(brd[:, zeros[z][1]], num) and not check_sub_group(zeros[z], brd, num):
                brd[zeros[z]] = num
                break
            else:
                num += 1
        if num >= 10:
            brd[zeros[z]] = 0
            z -= 1
        else:
            z += 1
    brd = brd.tolist()
    return brd


def check_sub_group(pos, brd, num):
    for i in range(len(brd)):  # catch row
        if pos[0] // 3 == i // 3:
            for j in range(len(brd[0])):  # catch column
                if pos[1] // 3 == j // 3:
                    if num == brd[i][j]:
                        return True
    return False


def check_row_column(array, num):
    for i in array:
        if i == num:
            return True
    return False


def get_empty(brd):
    list = []
    for i in range(len(brd)):  # catch row
        for j in range(len(brd[0])):  # catch column
            if brd[i][j] == 0:
                list.append((i, j))
    return list


eel.start('index.html', size=(450, 550))
