from collections import defaultdict
import time

def around(p):
    c, r, d, curr_cost = p
    if d == 'r':
        return [(c+1, r, d, curr_cost+1), (c, r, 'u', curr_cost+1000), (c, r, 'd', curr_cost+1000)]
    elif d == 'd':
        return [(c, r+1, d, curr_cost+1), (c, r, 'l', curr_cost+1000), (c, r, 'r', curr_cost+1000)]
    elif d == 'l':
        return [(c-1, r, d, curr_cost+1), (c, r, 'u', curr_cost+1000), (c, r, 'd', curr_cost+1000)]
    elif d == 'u':
        return [(c, r-1, d, curr_cost+1), (c, r, 'l', curr_cost+1000), (c, r, 'r', curr_cost+1000)]

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

    while queue:
        # print(queue)
        s = queue.pop()
        if costs[posdir(s)] <= s[3]:
            continue
        elif costs[posdir(s)] > s[3]:
            costs[posdir(s)] = s[3]

        next_states = accessible(s, map)
        queue += next_states
        print(len(queue))
    time.sleep(0.05)
    print_map(map, costs, s)

    e0, e1 = end
    return min((costs[(e0, e1, 'u')], costs[(e0, e1, 'd')], costs[(e0, e1, 'l')], costs[(e0, e1, 'r')]))

def print_map(map, costs, s):
    visited = set([pos(p) for p in costs])
    for r in range(140):
        for c in range(140):
            if (c, r) == pos(s):
                print("X", end="")
            elif (c, r) in visited:
                print("O", end="")
            else:
                print(map[(c, r)], end="")
        print()

with open("input", 'r') as f:
    
    lines = [l.strip() for l in f.readlines()]

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
    start_state = (start[0], start[1], curr_dir, 0)
    print("start", start_state)
    print("end", end)

    print(explore(start_state, map, costs, end))