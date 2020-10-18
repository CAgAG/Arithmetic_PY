"""
    三个列表均是升序
    (a, b, c)
    距离算法: max(abs(a-b), abs(a-c), abs(b-c))
"""
def MinDistance(a: list, b: list, c: list):
    ALen = len(a)
    BLen = len(b)
    CLen = len(c)

    minDis = 2**32

    i = 0
    j = 0
    k = 0
    while i < ALen:
        curDis = max(abs(a[i]-b[j]), abs(a[i]-c[k]), abs(b[j]-c[k]))
        if curDis < minDis:
            minDis = curDis

        minsd = min(a[i], b[j], c[k])
        if minsd == a[i]:
            i += 1
            if i >= ALen:
                break
        elif minsd == b[j]:
            j += 1
            if j >= BLen:
                break
        elif minsd == c[k]:
            k += 1
            if k >= CLen:
                break
    return minDis


if __name__ == '__main__':
    a = [i for i in range(10)]
    b = [i for i in range(8, 15)]
    c = [i for i in range(12, 30)]

    print(a)
    print(b)
    print(c)

    print(MinDistance(a, b, c))










