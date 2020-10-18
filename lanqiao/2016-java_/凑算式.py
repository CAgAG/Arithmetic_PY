import itertools

if __name__ == '__main__':
    count = 0
    for comb in itertools.permutations([i for i in range(1, 10)], 9):
        a = comb[0]
        b = comb[1]
        c = comb[2]
        DEF = comb[3] * 100 + comb[4] * 10 + comb[5]
        GHI = comb[6] * 100 + comb[7] * 10 + comb[8]

        if c == 0 or GHI == 0:
            continue
        if (a + b / c + DEF / GHI) == 10:
            count += 1

    print(count)
