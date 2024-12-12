from collections import defaultdict


def around(p):
    i, j = p
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]


def explore(p, map):
    c = map[p]
    region = set()
    region.add(p)
    q = [p for p in around(p) if map[p] == c]
    region.update(q)
    while q:
        p = q.pop()
        q += [m for m in around(p) if map[m] == c and m not in q and m not in region]
        region.update(q)

    return region


def perimeter(region):

    curr_perimeter = 0
    curr_p = set()

    for p in region:
        curr_p.add(p)
        curr_perimeter += 4 - len([m for m in around(p) if m in region])

    return curr_perimeter


with open("input.txt", 'r') as f:
    
    lines = [l.strip() for l in f.readlines()]

    map = defaultdict(str)

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            map[(j, i)] = c

    map_size = len(map)

    regions = []
    explored = set()

    while len(explored) != map_size:

        for i in range(len(lines)):
            for j in range(len(lines[0])):
                p = (j, i)
                if not p in explored:
                    r = explore(p, map)
                    regions.append(r)
                    explored.update(r)

    print(sum([len(r)*perimeter(r) for r in regions]))

        


    

