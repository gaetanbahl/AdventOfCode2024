import re

with open("input", 'r') as f:

    txt = "".join(f.readlines())

    r = """Button A: X.(\d+), Y.(\d+)
Button B: X.(\d+), Y.(\d+)
Prize: X.(\d+), Y.(\d+)"""

    res = re.findall(r, txt)

    s = 0
    for machine in res:
        m = [int(c) for c in machine]
        possibilities = []
        for i in range(101):
            for j in range(101):
                X = m[0]*i
                Y = m[1]*i
                X += m[2]*j
                Y += m[3]*j
                if X == m[4] and Y == m[5]:
                    possibilities.append(3*i+j)
        
        if possibilities:
            s += min(possibilities)

    print(s)