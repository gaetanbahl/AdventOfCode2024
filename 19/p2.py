from collections import defaultdict

FILE = "input.txt"

cache = dict()

def match(pattern, towels):

    if pattern in cache:
        return cache[pattern]

    if pattern == "":
        return 1
    
    total = 0

    for t in towels:
        if pattern.startswith(t):
            total += match(pattern[len(t):], towels)

    cache[pattern] = total
        
    return cache[pattern]

with open(FILE, 'r') as f:

    lines = f.readlines()

    towels = [t.strip() for t in lines[0].strip().split(",")]

    patterns = [l.strip() for l in lines[2:]]

    s = 0

    for p in patterns:
        print("PATTERN", p)
        res = int(match(p, towels))
        s += res
        if res:
            print("     MATCHED", res, "TIMES")
        else:
            print("     IMPOSSIBLE")

    print(s)