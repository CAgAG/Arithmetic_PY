if __name__ == '__main__':
    S = 0

    num = input()
    for i in range(1, int(num) + 1):
        S += str(i).count('1')

    print(S)