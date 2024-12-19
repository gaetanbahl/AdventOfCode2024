from collections import defaultdict
import time

GRID_SIZE = 70
N_BYTES = 1024
FILE = "input"

def around(p):
    c, r, curr_cost = p
    return [(c+1, r, curr_cost+1), (c-1, r, curr_cost+1), (c, r+1, curr_cost+1), (c, r-1, curr_cost+1)]

def accessible(p, map):
    a = around(p)
    return [p for p in a if map[pos(p)] == '.']

def pos(state):
    return (state[0], state[1])

def explore(state, map, costs, end):

    queue = accessible(state, map)
    costs[pos(state)] = 0

    while queue:
        # print(queue)
        s = queue.pop()
        if costs[pos(s)] <= s[2]:
            continue
        elif costs[pos(s)] > s[2]:
            costs[pos(s)] = s[2]

        next_states = accessible(s, map)
        queue += next_states
        # print(len(queue))
    time.sleep(0.05)
    print_map(map, costs, s)

    e0, e1 = end
    return costs[(e0, e1)]

def print_map(map, costs, s):
    visited = set([pos(p) for p in costs])
    for r in range(-1, GRID_SIZE+2):
        for c in range(-1, GRID_SIZE+2):
            if (c, r) == pos(s):
                print("X", end="")
            elif (c, r) in visited:
                print("O", end="")
            else:
                print(map[(c, r)], end="")
        print()

with open(FILE, 'r') as f:
    
    lines = [l.strip().split(',') for l in f.readlines()]

    map = defaultdict(lambda : '#')
    costs = defaultdict(lambda : 100000000000)

    for r in range(GRID_SIZE+1):
        for c in range(GRID_SIZE+1):
            map[(c, r)] = "."

    for l in lines[:N_BYTES]:
        map[(int(l[0]), int(l[1]))] = "#"
    
    start = (0, 0)
    end = (GRID_SIZE, GRID_SIZE)
    start_state = (start[0], start[1], 0)
    print("start", start_state)
    print("end", end)

    print(explore(start_state, map, costs, end))