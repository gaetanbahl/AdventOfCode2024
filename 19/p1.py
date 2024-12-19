FILE = "input.txt"

def match(pattern, towels):

    patterns = [pattern]

    while patterns:
        curr = patterns.pop()
        
        for t in towels:
            if curr.startswith(t):
                remaining = curr[len(t):]
                if remaining == "":
                    return True
                patterns.append(remaining)

    return False

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
            print("MATCHED")
        else:
            print("IMPOSSIBLE")

    print(s)