def bfs(target, operands):

    totals = [operands[0]]
    operands = operands[1:]

    while operands:

        operand = operands.pop(0)
        totals = [x * operand for x in totals] + [x + operand for x in totals]

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