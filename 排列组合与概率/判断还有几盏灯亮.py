"""
    灯拉动奇数次: 亮, 偶数次: 关
    拉动几次与约数有关
"""


# 计算约数
def Odd(num: int):
    count = 0
    i = 1
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1

    if count % 2 == 0:
        return 0
    return 1


def total(num: list, epoch: int):
    count = 0
    i = 0
    while i < epoch:
        if Odd(num[i]) == 1:
            count += 1
        i += 1
    return count


if __name__ == '__main__':
    arr = [
        i for i in range(1, 101)
    ]
    print(total(arr, 100))
