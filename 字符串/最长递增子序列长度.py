def GetMax(string: str):
    length = len(string)
    # 记录递增序列长度
    Lstr = [0] * length

    Lstr[0] = 1
    # 最大长度
    maxLen = 1

    i = 1
    while i < length:
        if string[i] > string[i-1]:
            Lstr[i] = Lstr[i-1] + 1
            if Lstr[i] > maxLen:
                maxLen = Lstr[i]
        else:
            Lstr[i] = 1
        i += 1

    return maxLen

if __name__ == '__main__':
    s = 'gabcdzefgzabc'

    print(GetMax(s))

