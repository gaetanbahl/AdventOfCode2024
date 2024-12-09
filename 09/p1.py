
def checksum(fs):
    return sum([i * v for i, v in enumerate(fs)])

with open("input", 'r') as f:

    lines = [x.strip() for x in f.readlines()]
    line = lines[0]

    fs = []
    id = 0
    for i, c in enumerate(line):
        
        if i%2:
            fs += [-1 for i in range(int(c))]
        else:
            fs += [id for i in range(int(c))]
            id += 1

    fs = list(fs)

    empty_spaces = [i for i,v in enumerate(fs) if v == -1]

    while empty_spaces:

        n = fs.pop()

        if n == -1:
            empty_spaces.pop()
        else:
            e = empty_spaces.pop(0)
            fs[e] = n

    print(checksum(fs))