import math
import sys
from functools import cache

sys.setrecursionlimit(1000)

N_BLINKS = 75

@cache
def n_digits(s):
    if s < 10:
        return 1
    else:
        return 1 + n_digits(s//10)

@cache
def split(s):
    s = str(s)
    a = len(s)//2
    return (int(s[:a]), int(s[a:]))

@cache
def comp(s, depth):

    if depth == 0:
        return 1
    else:
        if s == 0:
            return comp(1, depth-1)
        elif (n := n_digits(s)) % 2 == 0 :
            s1, s2 = split(s)
            return comp(s1, depth-1) + comp(s2, depth-1)
        else:
            return comp(s*2024, depth-1)


with open("input", 'r') as f:

    stones = f.readlines()[0].split()
    print(sum([comp(int(s), N_BLINKS) for s in stones]))