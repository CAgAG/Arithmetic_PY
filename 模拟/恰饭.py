import math

def f(Pnum, Wnum):
    Ps = []
    for _ in range(Pnum):
        Ps.append(int(input()))

    if Pnum < 2 * Wnum:
        print(min(Ps[:Wnum]))
        return

    Ps += [math.inf] * Wnum

    first = []
    second = []

    start = 0
    end = Wnum
    tWnum = Wnum
    while True:
        first = Ps[start: end]
        second = Ps[end: end + Wnum]

        first.sort()
        second.sort()

        if len(second) != tWnum:
            second += [math.inf] * (tWnum - len(second))

        for i in range(tWnum):
            second[i] += first[i]

        Ps[end: end+Wnum] = second

        start = end
        end += Wnum

        if start >= Pnum:
            break
        elif end >= Pnum:
            break
        elif (end + Wnum) >= Pnum:
            Wnum = (end + Wnum) - Pnum


    Time = min(second)

    print(Time)


if __name__ == '__main__':
    Pnum, Wnum = input().strip().split(' ')
    Pnum = int(Pnum)
    Wnum = int(Wnum)

    f(Pnum, Wnum)

