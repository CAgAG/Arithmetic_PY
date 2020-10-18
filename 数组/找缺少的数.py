"""
    1, 2...n, 数组元素排列
"""
import random


def GetNum(arr: list):
    if arr is None:
        return

    length = len(arr) + 1
    # 等差数列前n项和
    Sum = length + length * (length - 1) // 2  # 必为int
    return Sum - sum(arr)


# 异或
def GetNumXOR(arr: list):
    if arr is None:
        return

    a = arr[0]
    b = 1
    length = len(arr)

    # 缺失数组来一遍
    i = 1
    while i < length:
        a ^= arr[i]
        i += 1
    # 完整数组来一遍
    i = 2
    while i <= length + 1:
        b ^= i
        i += 1
    return a ^ b


if __name__ == '__main__':
    arr = [i for i in range(1, 10)]
    arr.pop(random.randint(1, 8))

    print(arr)
    print(GetNumXOR(arr))
