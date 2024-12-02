safe = 0

with open("input", 'r') as f:
    for l in f.readlines():
        l = list(map(int, l.split()))
        if l == sorted(l) or l == sorted(l, reverse=True):
            l1, l2 = l[:-1], l[1:]
            deltas = [abs(x-y) for x, y in zip(l1, l2)]
            if min(deltas) >= 1 and max(deltas) <= 3:
                safe += 1

print(safe)