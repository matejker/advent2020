import numpy as np


def jolts(filename="data/day10.dat"):
    with open(filename) as fdata:
        lines = np.array([0] + [int(l) for l in fdata.read().splitlines()])

    lines = np.sort(lines)
    differences = lines[1:] - lines[:-1]

    ones = sum(1 for i in differences if i == 1)
    threes = sum(1 for i in differences if i == 3) + 1

    return ones * threes


def get_arrange_number(filename="data/day10.dat"):
    with open(filename) as fdata:
        lines = np.array([0] + [int(l) for l in fdata.read().splitlines()])

    lines = np.sort(lines)
    differences = lines[1:] - lines[:-1]
    n = len(differences)
    count = 1

    perm_dict = {'2': 0, '3': 0, '1': 0}
    i = 0
    while i < n:
        if differences[i] != 1:
            i += 1
            continue

        j = i + 1
        row = 1
        while j < n and differences[j] == 1:
            row += 1
            j += 1

        if row == 2:
            count *= 2
            perm_dict['1'] += 1
        elif row == 3:
            count *= 4
            perm_dict['2'] += 1
        elif row == 4:
            count *= 7
            perm_dict['3'] += 1

        i = j + 1

    return count


assert jolts("data/day10-t.dat") == 220
assert get_arrange_number("data/day10-t.dat") == 19208

jolts()  # 2376
get_arrange_number()  # 129586085429248
