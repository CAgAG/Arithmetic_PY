"""
    已知随机函数
    1~7 均匀分布 -> 1~10 均匀分布
"""
import random


def rand7():
    return round(random.uniform(1, 7))


def ran10():
    while True:
        # 1~49
        x = (rand7() - 1) * 7 + rand7()
        # 截断: 1~40
        if x <= 40:
            break

    return x % 10 + 1


if __name__ == '__main__':
    print([ran10() for _ in range(10)])
