from collections import defaultdict
import numpy as np

GUARD_DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def update(guard_pos, guard_dir, grid):

    new_pos = tuple_add(guard_pos, GUARD_DIRS[guard_dir])

    if grid[new_pos] == "#":
        return (guard_pos, (guard_dir + 1) % 4)
    else:
        return(new_pos, guard_dir)


with open("input", 'r') as f:

    lines = [x.strip() for x in f.readlines()]
    grid = defaultdict(str)

    guard_pos = (0, 0)
    guard_dir = 0

    for j, l in enumerate(lines):
        for i, c in enumerate(l):
            if c == "#":
                grid[(i, j)] = c
            elif c == "^":
                guard_pos = (i, j)
                grid[(i, j)] = "."
            else:
                grid[(i, j)] = "."

    guard_pos_hist = set()

    #if original position counts as a position
    #guard_pos_hist.add((guard_pos, guard_dir))

    while True:
        guard_pos, guard_dir = update(guard_pos, guard_dir, grid)
        if grid[guard_pos] == '':
            break
        # if direction counts as different position
        #guard_pos_hist.add((guard_pos, guard_dir))
        guard_pos_hist.add(guard_pos)

print(len(guard_pos_hist))