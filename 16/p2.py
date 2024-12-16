from collections import defaultdict
import time

MAX_COL = 0
MAX_ROW = 0

def around(p):
    c, r, d, curr_cost, v = p
    if d == 'r':
        return [(c+1, r, d, curr_cost+1, v+[(c+1, r)]), (c, r, 'u', curr_cost+1000, v), (c, r, 'd', curr_cost+1000, v)]
    elif d == 'd':
        return [(c, r+1, d, curr_cost+1, v+[(c, r+1)]), (c, r, 'l', curr_cost+1000, v), (c, r, 'r', curr_cost+1000, v)]
    elif d == 'l':
        return [(c-1, r, d, curr_cost+1, v+[(c-1, r)]), (c, r, 'u', curr_cost+1000, v), (c, r, 'd', curr_cost+1000, v)]
    elif d == 'u':
        return [(c, r-1, d, curr_cost+1, v+[(c, r-1)]), (c, r, 'l', curr_cost+1000, v), (c, r, 'r', curr_cost+1000, v)]

def accessible(p, map):
    a = around(p)
    return [p for p in a if map[pos(p)] == '.']

def pos(state):
    return (state[0], state[1])

def posdir(state):
    return (state[0], state[1], state[2])

def explore(state, map, costs, end):

    queue = accessible(state, map)
    costs[posdir(state)] = 0

    paths_to_end = []

    while queue:
        # print(queue)
        s = queue.pop(0)
        if costs[posdir(s)] < s[3]:
            continue
        elif costs[posdir(s)] > s[3]:
            costs[posdir(s)] = s[3]        
            # print_map(map, costs, s, [])
            # time.sleep(0.05)

        next_states = accessible(s, map)
        queue += next_states

        if pos(s) == end:
            paths_to_end += [s]

    e0, e1 = end

    min_cost = min((costs[(e0, e1, 'u')], costs[(e0, e1, 'd')], costs[(e0, e1, 'l')], costs[(e0, e1, 'r')]))
    visited = set()
    print([p[3] for p in paths_to_end])
    print(min_cost)
    for p in paths_to_end:
        if p[3] == min_cost:
            visited.update(p[4])
    print_map(map, costs, s, visited)
    return len(visited)

def print_map(map, costs, s, paths_to_plot):
    visited = set([pos(p) for p in costs])
    for r in range(MAX_ROW):
        for c in range(MAX_COL):
            if (c, r) == pos(s):
                print("X", end="")
            elif (c, r) in visited:
                print("O", end="")
            # elif (c, r) in paths_to_plot:
            #     print("O", end="")
            else:
                print(map[(c, r)], end="")
        print()
    print()

with open("input", 'r') as f:
    
    lines = [l.strip() for l in f.readlines()]

    MAX_ROW = len(lines)
    MAX_COL = len(lines[0])

    map = defaultdict(str)
    costs = defaultdict(lambda : 100000000000)

    for r, l in enumerate(lines):
        for c, car in enumerate(l):
            map[(c, r)] = car
            if car == "E":
                map[(c, r)] = '.'
                end = (c, r)
            elif car == "S":
                map[(c, r)] = '.'
                start = (c, r)

    curr_dir = "r"
    start_state = (start[0], start[1], curr_dir, 0, [start])
    print("start", start_state)
    print("end", end)

    print(explore(start_state, map, costs, end))