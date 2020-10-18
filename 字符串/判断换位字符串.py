def Compare(s1: str, s2: str):
    d1 = dict()
    d2 = dict()

    for i, v in enumerate(s1):
        if d1.get(v) is None:
            d1[v] = 1
        else:
            d1[v] += 1

    for i, v in enumerate(s2):
        if d2.get(v) is None:
            d2[v] = 1
        else:
            d2[v] += 1
    return d1 == d2


if __name__ == '__main__':
    s1 = '123456'
    s2 = '431265'

    print(Compare(s1, s2))
