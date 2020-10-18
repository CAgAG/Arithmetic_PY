# 二进制位移
def isPow(n: int):
    if n < 1:
        return False
    i = 1
    while i <= n:
        if i == n:
            return True
        # 左移一位
        i <<= 1
    return False


# 与操作法
# 2**n -> 1, 10, 100, 1000, 10000 ...
def isPower(n: int):
    if n < 1:
        return False
    m = n & (n - 1)
    return m == 0


if __name__ == '__main__':
    n = 2 ** 8
    print(isPower(n))
