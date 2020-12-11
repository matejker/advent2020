from copy import deepcopy

POSITIONS = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]


def convert2list(string):
    list1 = []
    list1[:0] = string
    return list1


def get_neighbors(i, j, lines):
    n = len(lines)  # number of rows
    m = len(lines[0])  # number of columns

    count = 0
    for r, s in POSITIONS:
        k = i + r
        l = j + s
        if -1 < k < n and -1 < l < m:
            count += 1 if lines[k][l] == "#" else 0

    return count


def get_neighbors_tolerant(i, j, lines):
    n = len(lines)  # number of rows
    m = len(lines[0])  # number of columns

    count = 0
    for r, s in POSITIONS:
        c = 1
        k = i + r
        l = j + s
        while -1 < k < n and -1 < l < m:
            c += 1
            count += 1 if lines[k][l] == "#" else 0
            if lines[k][l] == "#" or lines[k][l] == "L":
                break
            k = i + c * r
            l = j + c * s

    return count


def game(lines, tolerance=3, neigh_func=get_neighbors):
    new = deepcopy(lines)
    n = len(lines)  # number of rows
    m = len(lines[0])  # number of columns

    for i in range(n):
        for j in range(m):
            neighbor = neigh_func(i, j, lines)
            if lines[i][j] == "#" and neighbor > tolerance:
                new[i][j] = "L"
            elif lines[i][j] == "L" and neighbor == 0:
                new[i][j] = "#"

    return new


def get_count(lines):
    count = 0
    for r in lines:
        for c in r:
            if c == "#":
                count += 1

    return count


def game_of_seats(filename="data/day11.dat"):
    with open(filename) as fdata:
        lines = [convert2list(l) for l in fdata.read().splitlines()]

    match = False
    pervioius_game = deepcopy(lines)
    while match is not True:
        new_game = game(pervioius_game)
        match = pervioius_game == new_game

        if not match:
            pervioius_game = deepcopy(new_game)

    return get_count(new_game)


def game_of_seats_tolerant(filename="data/day11.dat"):
    with open(filename) as fdata:
        lines = [convert2list(l) for l in fdata.read().splitlines()]

    match = False
    pervioius_game = deepcopy(lines)
    while match is not True:
        new_game = game(pervioius_game, 4, get_neighbors_tolerant)
        match = pervioius_game == new_game

        if not match:
            pervioius_game = deepcopy(new_game)

    return get_count(new_game)


assert game_of_seats(filename="data/day11-t.dat") == 37
assert game_of_seats_tolerant("data/day11-t.dat") == 26

game_of_seats()  # 2296
game_of_seats_tolerant()  # 2089
