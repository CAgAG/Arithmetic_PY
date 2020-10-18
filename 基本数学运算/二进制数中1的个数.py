# 移位法
def countOne(n: int):
    count = 0
    while n > 0:
        if (n & 1) == 1:  # 判断最后一位是否为1
            count += 1
        n >>= 1  # 移除最后一位
    return count


# 与操作法
def countOneI(n: int):
    count = 0
    while n > 0:
        if n != 0:  # 判断最后一位是否为1
            n = n & (n - 1)
        count += 1
    return count


if __name__ == '__main__':
    num = 7

    print(bin(7))
    print(countOne(num))
    print(countOneI(num))
