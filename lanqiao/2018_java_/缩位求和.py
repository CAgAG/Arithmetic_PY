def solver(num):
    s = sum([int(i) for i in str(num)])
    while s >= 10:
        s = sum([int(i) for i in str(s)])
    return s


if __name__ == '__main__':
    print(solver(7583676109608471656473500295825))
