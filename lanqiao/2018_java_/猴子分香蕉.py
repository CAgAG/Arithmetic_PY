if __name__ == '__main__':
    for num in range(1, 10000):
        if (num % 5 != 1): continue
        tpNum = num - 1 - (num // 5)
        if (tpNum % 5 != 2): continue
        tpNum = tpNum - 2 - tpNum // 5
        if (tpNum % 5 != 3): continue
        tpNum = tpNum - 3 - tpNum // 5
        if (tpNum % 5 != 4): continue
        tpNum = tpNum - 4 - tpNum // 5
        if (tpNum >= 5 and tpNum % 5 == 0):
            print(num)
            break
