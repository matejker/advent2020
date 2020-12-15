import re
from itertools import product


def translate_mem(command):
    z = re.match(r"mem\[(.[0-9]*)\] = (.[0-9]*)", command)
    g = z.groups()
    return int(g[0]), int(g[1])


def docking_data(filename="data/day14.dat"):
    with open(filename) as fdata:
        lines = fdata.read().splitlines()

    memory_units = []
    i = -1
    for l in lines:
        if "mask = " in l:
            i += 1
            memory_units.append({"mask": l[7:], "units": []})
        elif "mem[" in l:
            memory_units[i]["units"].append(translate_mem(l))

    mem = {}
    for m in memory_units:
        mask = m["mask"]
        for a in m["units"]:
            mem[a[0]] = (a[1] | int(mask.replace("X", "0"), 2)) & int(mask.replace("X", "1"), 2)

    return sum(v for k, v in mem.items())


def make_mask(base, holders, alt):
    return int(base + sum(2 ** n for n, a in zip(holders, alt) if a))


def possible_variations(filename="data/day14.dat"):
    with open(filename) as fdata:
        lines = fdata.read().splitlines()

    mem = {}
    for l in lines:
        if "mask = " in l:
            mask = l[7:]
            mask_inverted = int("".join("1" if v == "0" else "0" for v in mask), 2)
            base = int(mask.replace("X", "0"), 2)
            holders = [35 - k for k, v in enumerate(mask) if v == "X"]
            alternatives = list(product(range(2), repeat=len(holders)))
            masks = [make_mask(base, holders, alt) for alt in alternatives]
        else:
            for m in masks:
                a = translate_mem(l)
                mem[mask_inverted & a[0] | m] = a[1]

    return sum(v for k, v in mem.items())