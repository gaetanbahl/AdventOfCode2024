from collections import defaultdict

MAX_COL = 102
MAX_ROW = 51

def next_pos(pos, move):
    if move == "<":
        return (pos[0]-1, pos[1])
    elif move == "^":
        return (pos[0], pos[1]-1)
    elif move == "v":
        return (pos[0], pos[1]+1)
    elif move == ">":
        return (pos[0]+1, pos[1])

def move_obj(pos, move, map):

    new_pos = next_pos(pos, move)

    if map[new_pos] == '#':
        return False
    elif map[new_pos] == '.':
        map[new_pos] = map[pos]
        map[pos] = '.'
        return True
    elif map[new_pos] == 'O':
        has_moved = move_obj(new_pos, move, map)
        if has_moved:
            map[new_pos] = map[pos]
            map[pos] = '.'
            return True
        else:
            return False
    
    return False

def gps(pos):
    return 100*pos[1] + pos[0]


def print_map(map):
    for r in range(MAX_ROW):
        for c in range(MAX_COL):
            print(map[(c, r)], end="")
        print()

with open("input", 'r') as f:
    
    lines = [l.strip() for l in f.readlines()]

    map = defaultdict(str)

    for i, l in enumerate(lines):
        if l == "":
            max_row = i
            break
        for j, c in enumerate(l):
            map[(j, i)] = c
            if c == "@":
                robot_pos = (j, i)

    moves = "".join(lines[i:])

    # print_map(map)
    for m in moves:
        ret = move_obj(robot_pos, m, map)
        # print_map(map)
        if ret:
            robot_pos = next_pos(robot_pos, m)


    print(sum([gps(p) for p in map.keys() if map[p] == 'O']))

    

        


    

