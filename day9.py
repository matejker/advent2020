from itertools import permutations


def valid(preamble):
    return {sum(pair) for pair in permutations(preamble, 2)}


def xmas(filename="data/day9.dat", preamble_size=25):
    with open(filename) as fdata:
        lines = [int(l) for l in fdata.read().splitlines()]

    for i, line in enumerate(lines):
        if i < preamble_size:
            continue

        preamble = lines[i - preamble_size:i]
        if max(preamble) * 2 < line or min(preamble) * 2 > line:
            return line

        if line not in valid(preamble):
            return line

    return False


def encryption_weakness_xmas(filename="data/day9.dat", result=26796446):
    with open(filename) as fdata:
        lines = [int(l) for l in fdata.read().splitlines()]
    for i, line in enumerate(lines):
        j = i + 2
        while sum(lines[i:j]) < result:
            j += 1
        if sum(lines[i:j]) == result:
            return min(lines[i:j]) + max(lines[i:j])

    return False


assert xmas("data/day9-t.dat", 5) == 127
assert encryption_weakness_xmas("data/day9-t.dat", 127) == 62

xmas()  # 26796446
encryption_weakness_xmas()  # 3353494
