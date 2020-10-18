# pos 进位处理
def carry(num: list, pos: int):
    while pos > 0:
        if int(num[pos]) == 9:
            num[pos] = '0'
            num[pos - 1] = str(int(num[pos - 1]) + 1)
        pos -= 1


def findMinNonDup(n: int):
    nChars = list(str(n + 1))
    ch = [''] * (len(nChars) + 1)
    ch[0] = '0'
    i = 0
    while i < len(nChars):
        ch[i + 1] = nChars[i]
        i += 1

    lens = len(ch)
    i = 2  # 从左向右遍历
    while i < lens:
        # 相邻重复
        if ch[i - 1] == ch[i]:
            ch[i] = str(int(ch[i]) + 1)  # 末尾数字加1
            carry(ch, i)  # 处理进位
            # 把下标为i的后面字符串变为0101...串
            j = i + 1
            while j < lens:
                if (j - i) % 2 == 1:
                    ch[j] = '0'
                else:
                    ch[j] = '1'
                j += 1
        else:
            i += 1
    return ''.join(ch)


if __name__ == '__main__':
    print(findMinNonDup(23345))
