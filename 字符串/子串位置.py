# KMP 算法
# 求字符串的next 数组
def GetNext(p: str, Nexts: list):
    i = 0
    j = -1
    Nexts[0] = -1
    while i < len(p):
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            Nexts[i] = j
        else:
            j = Nexts[j]


def Match(s: str, p: str, Nexts: list):
    if (s or p) is None:
        return -1

    lens = len(s)
    lenp = len(p)

    if lens < lenp:
        return -1

    i = 0
    j = 0
    while i < lens and j < lenp:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = Nexts[j]

    if j >= lenp:
        return i - lenp

    return -1


if __name__ == '__main__':
    s = 'abababababaabcbab'
    p = 'abaabc'

    Nexts = [0] * (len(p) + 1)
    GetNext(p, Nexts)
    print(Nexts)
    print(Match(s, p, Nexts))
    print(s.index(p))
