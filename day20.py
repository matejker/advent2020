from operator import mul
from functools import reduce


def product(iterable):
    return reduce(mul, iterable, 1)


def parse_tile(tile_list):
    tile_id, tile = tile_list.split(":")
    tile = tile.split()
    return tile_id[5:], [
        tile[0],
        tile[-1],
        "".join([t[0] for t in tile]),
        "".join([t[-1] for t in tile])
    ]


def tile_intersection(t1, t2):
    count = 0
    for t in t1:
        count += 1 if t in t2 or t[::-1] in t2 else 0

    return count


def jurassic_jigsaw(filename="data/day20.dat"):
    data = open(filename).read().split("\n\n")
    tiles = {}

    for t in data:
        tile_id, tile = parse_tile(t)
        tiles[tile_id] = tile

    corners = []
    max_inter = {t: [] for t in tiles}
    for t in tiles:
        for tt in tiles:
            if tt == t:
                continue
            inter = tile_intersection(tiles[t], tiles[tt])
            max_inter[t].append(inter)
            max_inter[tt].append(inter)

    for m in max_inter:
        if sum(max_inter[m]) == 4:
            corners.append(int(m))

    return product(corners)


jurassic_jigsaw()
