import re

with open("input.txt", 'r') as f:
    txt = "".join(map(lambda x : x.strip(), f.readlines()))
    r = re.findall("mul\\((\\d*),(\\d*)\\)|(do\\(\\))|(don't\\(\\))", txt)

    sum = 0
    enable = True
    for match in r:
        if match[2] == "do()":
            enable=True
        elif match[3] == "don't()":
            enable=False
        else:
            if enable:
                sum += int(match[0]) * int(match[1])

print(sum)