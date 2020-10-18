# e: 精度要求
def sqrt(n: int, e: float):
    new_n = n
    last = 1  # 第一个近似值1
    while new_n - last > e:
        new_n = (new_n + last) / 2
        last = n / new_n
    return new_n


if __name__ == '__main__':
    print(sqrt(50, .0001))
