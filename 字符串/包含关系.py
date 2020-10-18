def isIn(s1: str, s2: str):
    d2 = dict()

    for s in s2:
        if d2.get(s) is None:
            d2[s] = 1
        else:
            d2[s] += 1

    for s in s1:
        if d2.get(s) is not None:
            d2[s] -= 1
            if d2[s] == 0:
                d2.pop(s)

    if d2:
        return False
    return True


if __name__ == '__main__':
    s1 = '123456'
    s2 = '573'
    print(isIn(s1, s2))
