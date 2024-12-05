from collections import defaultdict

with open("input", 'r') as f:

    lines = [x.strip() for x in f.readlines()]

    rules = defaultdict(list)
    updates = []

    n_rules = 0

    for r in lines:
        if len(r) == 0:
            break
        rule = list(map(int, r.split('|')))
        rules[rule[0]].append(rule[1])
        n_rules += 1

    for u in lines[n_rules+1:]:
        updates.append(list(map(int, u.split(','))))

    sum = 0

    for u in updates:
        valid = True
        middle = u[len(u)//2]
        while len(u):
            n = u.pop()
            for p in rules[n]:
                if p in u:
                    valid = False
                    break

            if not valid:
                break
        
        if valid:
            sum += middle

    print(sum)