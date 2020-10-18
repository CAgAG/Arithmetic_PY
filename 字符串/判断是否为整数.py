def isInt(Str: str):
    if Str is None:
        return None

    i = 0
    flag = False
    # 跳过符号
    if Str[0] == '-':
        i = 1
        flag = True
    elif Str[0] == '+':
        i = 1

    sums = 0
    for s in Str[i:]:
        if not s.isdecimal():
            return None
        else:
            sums = sums * 10 + int(s)

    if flag:
        sums *= -1
    return sums


if __name__ == '__main__':
    s1 = '+1234'
    s2 = '-1212'
    s3 = '1234'
    s4 = '++132'

    print(isInt(s1))
    print(isInt(s2))
    print(isInt(s3))
    print(isInt(s4))

