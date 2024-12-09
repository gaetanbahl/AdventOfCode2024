import math

def concat(n, m):
    l = math.ceil(math.log(m, 10))
    return int(n * math.pow(10, l) + m)

def bfs(target, operands):

    totals = [operands[0]]
    operands = operands[1:]

    while operands:

        operand = operands.pop(0)
        totals = [x * operand for x in totals] + [x + operand for x in totals] + [concat(x, operand) for x in totals]
        # totals = [x * operand for x in totals] + [x + operand for x in totals] + [int(f"{x}{operand}")  for x in totals]

    if target in totals:
        return target
    else:
        return 0


with open("input", 'r') as f:

    lines = [x.strip() for x in f.readlines()]

    lines = map(lambda l : l.split(":"), lines)
    lines = map(lambda l : (int(l[0]), [int(i) for i in l[1].split()]), lines)

    res = sum(map(lambda x : bfs(x[0], x[1]), lines))

print(res)