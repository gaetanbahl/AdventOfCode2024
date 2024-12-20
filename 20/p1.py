from collections import defaultdict

GRID_SIZE = 142
FILE = "input.txt"

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
    
    lines = [l.strip() for l in f.readlines()]

    map = defaultdict(lambda : '#')
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
    
    start_state = (start[0], start[1], 0)

    base_time = explore(start_state, map, costs, end)
    print(base_time)
    s = 0

    map[(26, 49)] = '.'
    costs = defaultdict(lambda : 100000000000)
    # print_map(map, costs, start_state)
    new_time = explore(start_state, map, costs, end)
    print(new_time)
    map[(26, 49)] = '#'

    for r in range(1, len(lines)-1):
        for c in range(1, len(lines[0])-1):
            if map[(c, r)] == "#":
                # print(c, r)
                map[(c, r)] = "."
                costs = defaultdict(lambda : 100000000000)
                # print_map(map, costs, start_state)
                new_time = explore(start_state, map, costs, end)
                # print(new_time)
                map[(c, r)] = "#"
                if base_time - new_time >= 100:
                    s += 1
                    print("FOUND", c, r)

    print(s)
