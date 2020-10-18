import itertools

if __name__ == '__main__':
    count = 0
    for comb in itertools.permutations([i for i in range(1, 10)], 9):
        a = comb[0] + comb[1] + comb[3] + comb[5]
        b = comb[0] + comb[2] + comb[4] + comb[8]
        c = comb[5] + comb[6] + comb[7] + comb[8]
        if a == b and b == c:
            count += 1
    print(count//6)
