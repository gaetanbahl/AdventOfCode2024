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

    for upd in updates:
        valid = True
        u = upd.copy()
        new_u = []
        while len(u):
            n = u.pop()
            moved = False
            for p in rules[n]:
                if p in u:
                    valid = False
                    moved = True
                    u.insert(u.index(p), n)
                    break

            if not moved:
                new_u.append(n)
        
        if not valid:
            sum += new_u[len(new_u)//2]

    print(sum)