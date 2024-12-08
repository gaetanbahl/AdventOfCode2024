from collections import defaultdict
import numpy as np
from itertools import combinations


def antinode_coords(a, b):
    v = b - a
    return b + v, a - v

def in_bounds(a, max_x, max_y):
    return a[0] >= 0 and a[0] < max_x and a[1] >= 0 and a[1] < max_y

with open("input", 'r') as f:

    lines = [x.strip() for x in f.readlines()]

    antennas = defaultdict(list)
    antinodes = set()

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c not in ['.', '#']:
                antennas[c].append(np.array((j, i), dtype=np.int32))

    max_y, max_x = len(lines), len(lines[0])

    for a in antennas.values():
        for a1, a2 in combinations(a, 2):
            new_antinodes = antinode_coords(a1, a2)
            for n in new_antinodes:
                if in_bounds(n, max_x, max_y):
                    antinodes.add(tuple(n))

    print(len(antinodes)) 