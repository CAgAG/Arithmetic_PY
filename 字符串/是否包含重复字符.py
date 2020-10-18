def isDup(s: str):
    return len(s) != len(set(s))


def isDupI(s: str):
    dic = dict()
    for i in s:
        if dic.get(i) is None:
            dic[i] = 0
        else:
            return True
    return False


if __name__ == '__main__':
    s = 'asdfg'

    print(isDup(s))
    print(isDupI(s))
