# 找出最长的公共子串的长度
def GetLen(s1: str, s2: str):
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] == s2[i]:
            i += 1
        else:
            break

        i += 1
    return i


# 最长公共子串
def GetMaxCommonSub(Str: str):
    length = len(Str)
    # 存储后缀数组
    suff = [''] * length

    Len = 0
    SubStr = ''

    # 获得后缀数组
    i = 0
    while i < length:
        suff[i] = Str[i: ]
        i += 1
    # 对后缀数组排序
    suff.sort()
    i = 1
    while i < length:
        tp = GetLen(suff[i], suff[i - 1])
        if tp > Len:
            Len = tp
            SubStr = suff[i][0: i + 1]
        i += 1

    return SubStr

if __name__ == '__main__':
    s = 'banana'
    print(GetMaxCommonSub(s))
