def ChargeInter(s1: list, s2: list):
    min1 = s1[0]
    max1 = s1[1]

    min2 = s2[0]
    max2 = s2[1]

    if min1 < min2:
        if max1 < min2:
            return None
        elif max1 <= max2:
            return min2, max1
        else:
            return min2, max2
    elif min1 <= max2:
        if max1 <= max2:
            return min1, max1
        else:
            return min1, max2
    else:
        return None

def GetInter(s1: tuple, s2: tuple):
    result = []
    for l1 in s1:
        for l2 in s2:
            c = ChargeInter(l1, l2)
            if c is not None:
                result.append(c)

    return result


if __name__ == '__main__':
    S1 = (
        [4, 8], [9, 13]
    )
    S2 = (
        [6, 12],
    )

    result = GetInter(S1, S2)
    print(result)


