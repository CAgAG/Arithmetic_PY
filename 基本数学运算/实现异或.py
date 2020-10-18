def XOR(x, y):
    res = 0
    i = 32 - 1
    while i >= 0:
        # 获取当前bit值
        b1 = (x & (1 << i)) > 0
        b2 = (y & (1 << i)) > 0

        if b1 == b2:
            xoredBit = 0
        else:
            xoredBit = 1

        res <<= 1
        res |= xoredBit
        i -= 1
    return res


if __name__ == '__main__':
    print(XOR(3, 5))
