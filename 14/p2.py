import re
import numpy as np

# MAX_COL, MAX_ROW = 11, 7
MAX_COL, MAX_ROW = 101, 103
STEPS = 1000000

def move(r):
    return ((r[0] + r[2]) % MAX_COL, (r[1] + r[3]) % MAX_ROW, r[2], r[3])

def print_grid(robots):

    robots = [(r[0], r[1]) for r in robots]

    for r in range(MAX_ROW):
        for c in range(MAX_COL):
            if (c, r) in robots:
                print('x', end="")
            else:
                print(".", end="")
        print()


def std(robots):
    norms = [np.linalg.norm(np.array((r[0], r[1])), 2) for r in robots]
    return np.std(norms)

with open("input", 'r') as f:

    txt = "".join(f.readlines())

    r = """p=(\d+),(\d+) v=(-?\d+),(-?\d+)"""

    res = re.findall(r, txt)

    robots = [tuple([int(i) for i in r]) for r in res]

    std_col, std_row = [], []

    min_std = 100000

    for s in range(STEPS):
        robots = list(map(move, robots))

        if (m := std(robots)) < min_std:
            min_std = m
            print(s, min_std)
            print_grid(robots)