from collections import defaultdict
import time

MAX_COL = 102
MAX_ROW = 50

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
        return []
    elif map[new_pos] == '.':
        return [(pos, new_pos)]
    elif map[new_pos] in ['[', ']'] and move in ['<', '>']:
        to_be_moved = move_obj(new_pos, move, map)
        if to_be_moved:
            to_be_moved.append((pos, new_pos))
            return to_be_moved
        else:
            return []
    elif map[new_pos] in ['[', ']'] and move in ['^', 'v']:
        shift = 1 if map[new_pos] == '[' else -1
        pos_other = (new_pos[0]+shift, new_pos[1])
        to_be_moved_other = move_obj(pos_other, move, map)
        if to_be_moved_other:
            to_be_moved = move_obj(new_pos, move, map)
            if to_be_moved:
                return to_be_moved_other + [t for t in to_be_moved if not t in to_be_moved_other] + [(pos, new_pos)]
    return []

def commit_moves(moves, map):
    for m in moves:
        map[m[1]] = map[m[0]]
        map[m[0]] = '.'

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
            if c == "@":
                map[(2*j, i)] = c
                map[(2*j+1, i)] = '.'
                robot_pos = (2*j, i)
            elif c == ".":
                map[(2*j, i)] = '.'
                map[(2*j+1, i)] = '.'
            elif c == "O":
                map[(2*j, i)] = '['
                map[(2*j+1, i)] = ']'
            elif c == "#":
                map[(2*j, i)] = '#'
                map[(2*j+1, i)] = '#'


    moves = "".join(lines[i:])

    print_map(map)
    for m in moves:
        move_list = move_obj(robot_pos, m, map)
        # print(m, move_list)
        commit_moves(move_list, map)
        print("\n\n")
        print_map(map)
        # input()
        if move_list:
            robot_pos = next_pos(robot_pos, m)
        
        time.sleep(0.15)


    print(sum([gps(p) for p in map.keys() if map[p] == '[']))

    

        


    

