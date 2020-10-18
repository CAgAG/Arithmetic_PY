import math


def Area(r):
    return math.pi * (r ** 2)


if __name__ == '__main__':
    r = int(input())

    print('{:.7f}'.format(Area(r)))
