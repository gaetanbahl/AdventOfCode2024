

def dv(reg, combo):
    STATE[reg] = int(STATE[0] / (2**combo_value(combo)))
    STATE[-1] += 2

adv = lambda combo : dv(0, combo)

def bxl(lit):
    STATE[1] ^= lit
    STATE[-1] += 2

def bst(combo):
    STATE[1] = combo_value(combo) % 8
    STATE[-1] += 2

def jnz(lit):
    if STATE[0]:
        STATE[-1] = lit
    else:
        STATE[-1] += 2

def bxc(operand):
    STATE[1] =  STATE[1] ^ STATE[2]
    STATE[-1] += 2

def out(combo):
    OUTPUT.append(combo_value(combo) % 8)
    STATE[-1] += 2

bdv = lambda combo : dv(1, combo)
cdv = lambda combo : dv(2, combo)

def combo_value(combo):
    vals = [0, 1, 2, 3, STATE[0], STATE[1], STATE[2], "NOPE"]
    return vals[combo]

OUTPUT = []

ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

with open("input", 'r') as f:

    lines = f.readlines()

    A = int(lines[0].split()[-1])
    B = int(lines[1].split()[-1])
    C = int(lines[2].split()[-1])

    pgm = [int(i) for i in lines[-1].split()[-1].split(',')]

    # print(A, B, C)
    # print(pgm)

    STATE = [A, B, C, 0]

    while STATE[-1] < len(pgm):
        # print(STATE, ops[pgm[STATE[-1]]], pgm[STATE[-1]+1])
        ops[pgm[STATE[-1]]](pgm[STATE[-1]+1])


    print(",".join(map(str, OUTPUT)))

