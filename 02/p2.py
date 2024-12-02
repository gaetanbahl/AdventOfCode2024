safe = 0

with open("input", 'r') as f:
    for l in f.readlines():
        l = list(map(int, l.split()))
        for i in range(len(l)):
            drop = l.copy()
            drop.pop(i)
            if drop == sorted(drop) or drop == sorted(drop, reverse=True):
                l1, l2 = drop[:-1], drop[1:]
                deltas = [abs(x-y) for x, y in zip(l1, l2)]
                if min(deltas) >= 1 and max(deltas) <= 3:
                    safe += 1
                    break

print(safe)