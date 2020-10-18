def GetMaxSubStr(str1: str, str2: str):
    length1 = len(str1)
    length2 = len(str2)

    sub = ''

    # 最大公共子串长度
    maxLen = 0
    # 最大公共子串, 结束位置
    maxLenEnd1 = 0

    i = 0
    while i < length1 + length2:
        s1begin = s2begin = 0
        tpMaxlen = 0
        if i < length1:
            s1begin = i
        else:
            s2begin = i - length1

        # 共同前进的步数
        j = 0
        while s1begin + j < length1 and s2begin + j < length2:
            # 对应字符相等
            if str1[s1begin + j] == str2[s2begin + j]:
                tpMaxlen += 1
            else:
                # 更新最大长度及位置
                if tpMaxlen > maxLen:
                    maxLen = tpMaxlen
                    maxLenEnd1 = s1begin + j
                else:
                    tpMaxlen = 0
            j += 1

        if tpMaxlen > maxLen:
            maxLen = tpMaxlen
            maxLenEnd1 = s1begin + j
        i += 1

    i = maxLenEnd1 - maxLen
    while i < maxLenEnd1:
        sub += str1[i]
        i += 1
    return sub


if __name__ == '__main__':
    str1 = 'akksdfgs'
    str2 = 'ksdfg'
    print(GetMaxSubStr(str1, str2))
