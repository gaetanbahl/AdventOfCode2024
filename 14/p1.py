import re

# MAX_COL, MAX_ROW = 11, 7
MAX_COL, MAX_ROW = 101, 103
STEPS = 100

def move(r):
    return ((r[0] + r[2]) % MAX_COL, (r[1] + r[3]) % MAX_ROW, r[2], r[3])


def count_quadrants(robots):
    mid_c = MAX_COL // 2
    mid_r = MAX_ROW // 2
    print(mid_c, mid_r)

    top_left, top_right, bot_left, bot_right = 0, 0, 0, 0

    for r in robots:
        if r[0] < mid_c and r[1] < mid_r:
            top_left += 1
        elif r[0] > mid_c and r[1] < mid_r:
            top_right += 1
        elif r[0] < mid_c and r[1] > mid_r:
            bot_left += 1
        elif r[0] > mid_c and r[1] > mid_r:
            bot_right += 1
    print(top_left, top_right, bot_left, bot_right)
    return  top_left * top_right * bot_left * bot_right
        
 
with open("input", 'r') as f:

    txt = "".join(f.readlines())

    r = """p=(\d+),(\d+) v=(-?\d+),(-?\d+)"""

    res = re.findall(r, txt)

    robots = [tuple([int(i) for i in r]) for r in res]

    for s in range(STEPS):
        robots = list(map(move, robots))

    print(count_quadrants(robots))