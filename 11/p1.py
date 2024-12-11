N_BLINKS = 25
    
def n_digits(s):
    if s < 10:
        return 1
    else:
        return 1 + n_digits(s//10)

def split(s, a):
    s = str(s)
    return [int(s[:a]), int(s[a:])]

with open("input", 'r') as f:

    line = f.readlines()[0]
    stones = list(map(int, line.split()))

    for i in range(N_BLINKS):
        new_stones = []
        for s in stones:
            if s == 0:
                new_stones.append(1)
            elif (n := n_digits(s)) % 2 == 0 :
                new_stones += split(s, n//2)
            else:
                new_stones.append(s*2024)

        stones = new_stones

    print(len(stones))