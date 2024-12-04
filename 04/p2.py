from collections import defaultdict

d = defaultdict(lambda : '.')

def check(x, y, d):

    s = 0

    if d[(x, y)] == "A":
        if d[(x+1, y+1)] == 'M' and d[(x-1, y+1)] == 'M' and d[(x+1, y-1)] == 'S' and d[(x-1, y-1)] == 'S':
            s += 1
        if d[(x-1, y-1)] == 'M' and d[(x+1, y-1)] == 'M' and d[(x+1, y+1)] == 'S' and d[(x-1, y+1)] == 'S':
            s += 1
        if d[(x-1, y-1)] == 'M' and d[(x-1, y+1)] == 'M' and d[(x+1, y+1)] == 'S' and d[(x+1, y-1)] == 'S':
            s += 1
        if d[(x+1, y+1)] == 'M' and d[(x+1, y-1)] == 'M' and d[(x-1, y+1)] == 'S' and d[(x-1, y-1)] == 'S':
            s += 1
        
    return s

with open("sample", 'r') as f:
    lines = list(map(lambda x : x.strip(), f.readlines()))

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            d[(i, j)] = c
    sum = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            sum += check(i, j, d)

print(sum)