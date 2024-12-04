from collections import defaultdict

d = defaultdict(lambda : '.')

def check(x, y, d):

    s = 0

    if d[(x, y)] == "X":
        if d[(x, y+1)] == 'M' and d[(x, y+2)] == 'A' and d[(x, y+3)] == 'S':
            s += 1
        if d[(x, y-1)] == 'M' and d[(x, y-2)] == 'A' and d[(x, y-3)] == 'S':
            s += 1
        if d[(x-1, y-1)] == 'M' and d[(x-2, y-2)] == 'A' and d[(x-3, y-3)] == 'S':
            s += 1
        if d[(x+1, y-1)] == 'M' and d[(x+2, y-2)] == 'A' and d[(x+3, y-3)] == 'S':
            s += 1
        if d[(x-1, y+1)] == 'M' and d[(x-2, y+2)] == 'A' and d[(x-3, y+3)] == 'S':
            s += 1
        if d[(x+1, y+1)] == 'M' and d[(x+2, y+2)] == 'A' and d[(x+3, y+3)] == 'S':
            s += 1
        if d[(x-1, y)] == 'M' and d[(x-2, y)] == 'A' and d[(x-3, y)] == 'S':
            s += 1
        if d[(x+1, y)] == 'M' and d[(x+2, y)] == 'A' and d[(x+3, y)] == 'S':
            s += 1
        
    return s

with open("input", 'r') as f:
    lines = list(map(lambda x : x.strip(), f.readlines()))

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            d[(i, j)] = c
    sum = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            sum += check(i, j, d)

print(sum)