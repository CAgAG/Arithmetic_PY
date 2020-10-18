def GetLargestSub(src: str):
    if src is None:
        return None

    length = len(src)
    retSub = [''] * (length + 1)

    i = 0
    k = 0
    while i < length:
        retSub[k] = src[i]
        j = i + 1
        while j < length:
            # 找出第i个字符后面最大的字符放到retSub
            if src[j] > retSub[k]:
                retSub[k] = src[j]
                # 位置移动
                i = j
            j += 1
        k += 1
        i += 1
    return ''.join(retSub[: k])


if __name__ == '__main__':
    s = 'acbdxmng'

    print(GetLargestSub(s))
