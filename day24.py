# Axial coordinates
# https://www.redblobgames.com/grids/hexagons/#coordinates-axial
# e, se, sw, w, nw, and ne
from collections import Counter
from itertools import product
from copy import deepcopy
from operator import add


def lobby_layout(filename="data/day24.dat"):
    tiles = open(filename).read().split()
    coordinates = []
    for t in tiles:
        r, q = 0, 0
        while len(t) > 0:
            if t[0] == "e":
                q += 1
                t = t[1:]
            elif t[0] == "w":
                q -= 1
                t = t[1:]
            elif t[:2] == "se":
                r += 1
                t = t[2:]
            elif t[:2] == "sw":
                q -= 1
                r += 1
                t = t[2:]
            elif t[:2] == "nw":
                r -= 1
                t = t[2:]
            elif t[:2] == "ne":
                q += 1
                r -= 1
                t = t[2:]
        coordinates.append((r, q))
        c = Counter(coordinates)
    return sum(i % 2 for i in c.values()), c


def tuple_sum(t1, t2):
    return tuple(map(add, t1, t2))


def maxmin(matrix):
    max_v = 0
    min_v = 0

    for m in matrix:
        for i in m:
            max_v = i if i > max_v else max_v
            min_v = i if i < min_v else min_v
    return max(abs(max_v), abs(min_v))


def game_of_lobby(filename="data/day24.dat"):
    _, tiles = lobby_layout(filename)
    tiles = {k: v % 2 for k, v in tiles.items()}
    black = {k for k, v in tiles.items() if v}
    position = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1)]
    for _ in range(100):
        new = set()
        m = maxmin(black)
        world = list(product(range(-m - 1, m + 2), repeat=2))
        for t in world:
            count = 0
            for p in position:
                count += 1 if tuple_sum(p, t) in black else 0
            if t in black and 1 <= count <= 2:
                new.add(t)
            elif t not in black and count == 2:
                new.add(t)
        black = deepcopy(new)

    return len(black)


game_of_lobby()  # 228
lobby_layout()  # 3672
