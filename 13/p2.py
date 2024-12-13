import re
import numpy as np

with open("input", 'r') as f:

    txt = "".join(f.readlines())

    r = """Button A: X.(\d+), Y.(\d+)
Button B: X.(\d+), Y.(\d+)
Prize: X.(\d+), Y.(\d+)"""

    res = re.findall(r, txt)

    s = 0
    for machine in res:
        m = [int(c) for c in machine]

        A = np.array([[m[0], m[2]],[m[1], m[3]]])
        b = np.array([10000000000000+m[4], 10000000000000+m[5]])

        x = np.linalg.solve(A, b)

        i = int(np.round(x[0]))
        j = int(np.round(x[1]))

        if m[0]*i+m[2]*j == m[4]+10000000000000 and m[1]*i+m[3]*j == m[5]+10000000000000:
            s += 3*i + j

    print(s)