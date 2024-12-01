with open("input", 'r') as f:
    lines = [tuple(l.split()) for l in f.readlines()]
    l1, l2 = list(zip(*lines))
    l1 = sorted(map(int, l1))
    l2 = sorted(map(int, l2))
    dist = sum([x * l2.count(x) for x in l1])
    print(dist)