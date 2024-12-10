from collections import defaultdict


def next(pos, grid):
    options = []
    n = grid[pos]
    i, j = pos

    if grid[(i+1, j)] == n+1:
        options.append((i+1, j))
    if grid[(i-1, j)] == n+1:
        options.append((i-1, j))
    if grid[(i, j+1)] == n+1:
        options.append((i, j+1))
    if grid[(i, j-1)] == n+1:
        options.append((i, j-1))
    
    return options

def reachable(pos, grid, memo):

    if pos in memo:
        return memo[pos]

    if grid[pos] == 9:
        memo[pos] = 1
        return memo[pos]
    else:
        s = 0
        opt = next(pos, grid)
        for o in opt:
            s += reachable(o, grid, memo)
        memo[pos] = s
        return s


with open("input", 'r') as f:

    lines = [x.strip() for x in f.readlines()]
    grid = defaultdict(lambda : -1)

    trailheads = []

    for i,l in enumerate(lines):
        for j,c in enumerate(l):
            c = int(c)
            grid[(j, i)] = c
            if c == 0:
                trailheads.append((j, i))


    memo = dict()

    print(sum([reachable(t, grid, memo) for t in trailheads]))