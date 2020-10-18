"""
    注: len(a) == n
    b[i] = a[0]*a[1]*a[2]...*a[n-1]/a[i]
    == 不乘a[i]
"""


def Calculate(a: list, b: list):
    b[0] = 1
    length = len(a)

    """
    [a1, a2, ai, ai+1, ai+2]
    正向: b[i] = a1*a2 
    反向: b[i] *= (ai+1 * ai+2)
    """
    # 正向乘积
    i = 1
    while i < length:
        b[i] = b[i - 1] * a[i - 1]
        i += 1

    b[0] = a[length - 1]
    # b[n] 不用管了
    i = length - 2
    while i >= 1:
        b[i] *= b[0]
        b[0] *= a[i]  # 逆向计算乘积
        i -= 1


if __name__ == '__main__':
    a = [
        i for i in range(2, 11)
    ]
    b = [None] * len(a)

    Calculate(a, b)

    print(a)
    print(b)

    sums = 1
    for i in range(2, 11):
        sums *= i
    print(sums)
