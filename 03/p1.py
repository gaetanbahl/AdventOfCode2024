import re

with open("input.txt", 'r') as f:
    txt = "".join(map(lambda x : x.strip(), f.readlines()))
    r = re.findall("mul\\((\\d*),(\\d*)\\)", txt)
    print(sum(map(lambda x : int(x[0])*int(x[1]), r)))