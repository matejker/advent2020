from operator import add
from itertools import product
from copy import deepcopy

TEST = """.#.
..#
###""".split("\n")
INPUT = """#...#...
#..#...#
..###..#
.#..##..
####...#
######..
...#..#.
##.#.#.#""".split("\n")


def tuple_sum(t1, t2):
    return tuple(map(add, t1, t2))


def position(dim):
    return list(set(product([-1, 0, 1], repeat=dim)) - {(0, ) * dim})


def maxmin(matrix):
    max_v = 0
    min_v = 0

    for m in matrix:
        for i in m:
            max_v = i if i > max_v else max_v
            min_v = i if i < min_v else min_v
    return max(abs(max_v), abs(min_v))


def create_world(world, dim=3):
    matrix = set()

    for i, row in enumerate(world):
        for j, c in enumerate(row):
            if c == "#":
                if dim == 4:
                    matrix.add((0, 0, i, j))
                else:
                    matrix.add((0, i, j))
    return matrix


def get_neighbours(matrix, coordinates, dim=3):
    count = 0

    for p in position(dim):
        s = tuple_sum(p, coordinates)
        count += 1 if s in matrix else 0
    return count


def game(matrix, dim):
    m = maxmin(matrix)
    world = product(range(-m - 1, m + 2), repeat=dim)
    new_matrix = deepcopy(matrix)
    for cell in world:
            count = get_neighbours(matrix, cell, dim)
        if cell in matrix and 1 < count < 4:
            new_matrix.add(cell)
        elif cell not in matrix and count == 3:
            new_matrix.add(cell)
        else:
            new_matrix.discard(cell)
    return new_matrix


def run(dim=3, rounds=6, world=INPUT):
    matrix = create_world(world, dim)
    for _ in range(rounds):
        matrix = game(matrix, dim)

    return len(matrix)


run()  # 252
run(4)  # 2160