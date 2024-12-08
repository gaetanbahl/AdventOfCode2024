from collections import defaultdict
import numpy as np
from itertools import combinations


def antinode_coords(a, b, max_x, max_y):
    v = b - a
    antinodes = []
    for i in range(max(max_x, max_y)):
        an = b + i*v
        if in_bounds(an, max_x, max_y):
            antinodes.append(an)
        else:
            break
    for i in range(max(max_x, max_y)):
        an = a - i*v
        if in_bounds(an, max_x, max_y):
            antinodes.append(an)
        else:
            break

    return map(tuple, antinodes)

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
            antinodes.update(antinode_coords(a1, a2, max_x, max_y))

    print(len(antinodes)) 