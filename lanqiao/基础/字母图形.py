import string

if __name__ == '__main__':
    upper = string.ascii_uppercase

    n, m = input().strip().split(' ')

    for i in range(int(n)):
        start = 1
        print(upper[i], end='')
        for j in range(1, int(m)):
            if i > j:
                print(upper[i - j], end='')
            elif i == j:
                print(upper[0], end='')
            else:
                print(upper[start], end='')
                start += 1
        print()

