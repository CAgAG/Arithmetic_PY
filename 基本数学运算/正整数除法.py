"""
    不用 /
"""


def div_mod(m: int, n: int):
    res = 0

    while m >= n:
        m -= n
        res += 1
    remain = m
    return res, remain


# 移位法
def div_mod2(m: int, n: int):
    res = 0
    while m >= n:
        multi = 1
        # multi * n > m / 2
        while multi * n <= (m >> 1):
            multi <<= 1
        m -= multi * n
        res += multi
    return res, m


# 变形
# 实现加法, 减法, 乘法
def Add(m: int, n: int):
    while True:
        # 保存不进位相加结果
        sums = m ^ n
        # 保存进位值
        carry = (m & n) << 1
        m = sums
        n = carry
        if carry == 0:
            break
    return sums


def Sub(m: int, n: int):
    return Add(m, Add(~n, 1))


def Multiply(m: int, n: int):
    # 正负标识
    neg = (m > 0) ^ (n > 0)

    # abs
    if n < 0:
        n = Add(~n, 1)
    if m < 0:
        m = Add(~m, 1)

    result = 0
    # key: 向左移动后的值, value: 移位的次数->位置编号
    bit_pos = dict()
    i = 0
    while i < 32:
        bit_pos[1 << i] = i

    while n > 0:
        # 计算最后一位1的位置编号
        pos = bit_pos[n & ~(n-1)]
        result += (m << pos)
        # 去掉最后一位1
        n &= n - 1

    if neg:
        result = Add(~result, 1)
    return result



if __name__ == '__main__':
    m = 10
    n = 2

    div, mod = divmod(m, n)
    print(div, mod)
    div, mod = div_mod(m, n)
    print(div, mod)
    div, mod = div_mod2(m, n)
    print(div, mod)

    print(Add(m, n))
