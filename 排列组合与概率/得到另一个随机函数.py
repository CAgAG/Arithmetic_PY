import random


# 0 , 1 概率 1/2
def Rfunc():
    return round(random.random())


# 0, 1 概率1/4 3/4
def NewRFunc():
    r1 = Rfunc()
    r2 = Rfunc()

    tp = r1
    tp |= r2 << 1
    # 00, 01, 10, 11
    if tp == 0:
        return 0
    return 1

if __name__ == '__main__':
    count = 1000
    print([
        Rfunc() for _ in range(count)
    ].count(1) / count)

    print([
        NewRFunc() for _ in range(count)
    ].count(1) / count)