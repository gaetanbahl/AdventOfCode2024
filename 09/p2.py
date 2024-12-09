
def checksum(files):
    s = 0
    for f in files:
        pos, id, size = f
        s += sum([f[1]*i for i in range(pos, pos+size)])
    return s

with open("input", 'r') as f:

    lines = [x.strip() for x in f.readlines()]
    line = lines[0]

    empty_spaces, files = [], []
    id = 0
    pos = 0
    for i, c in enumerate(line):
        size = int(c)
        if i%2:
            empty_spaces += [(pos, size)]
        else:
            files += [(pos, id, size)]
            id += 1
        pos += size
    
    updated_files = []
    for f in reversed(files):
        pos, id, length = f

        empty_spaces = sorted(empty_spaces, key=lambda x : x[0])
        empty_spaces = [(p, s) for p, s in empty_spaces if p < pos]

        moved = False
        for e in empty_spaces:

            if e[1] >= length:
                empty_spaces.remove(e)

                empty_space_pos, empty_space_size = e

                new_f = (empty_space_pos, id, length)
                updated_files.append(new_f)

                if length < empty_space_size:
                    new_e = (empty_space_pos + length, empty_space_size - length)
                    empty_spaces.append(new_e)
                moved = True
                break
        if not moved:
            updated_files.append(f)

    print(checksum(updated_files))