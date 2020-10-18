def find(arr, ele, start: int, end: int):
    index = []
    for i, v in enumerate(arr[start: end], start=start):
        if v == ele:
            index.append(i)
    return index


def GetLong(arr: str):
    if arr is None:
        return

    length = len(arr)

    if length == 1:
        return arr
    elif length == 2:
        if arr[0] == arr[1]:
            return 0, 1
        else:
            return -1, 0

    maxLen = 0
    index = -1

    i = 0
    while i < length - 2:
        indexs = find(arr, arr[i], i + 1, length)

        for pos in indexs:
            begin = i + 1
            end = pos - 1
            tpmax = 1
            while end != begin and end > begin:
                if arr[begin] == arr[end]:
                    begin += 1
                    end -= 1
                    tpmax += 1
                else:
                    break

            # 奇数
            if begin == end:
                tpmax = tpmax*2 + 1
                if tpmax > maxLen:
                    maxLen = tpmax
                    index = i
            # 偶数
            if begin - 1 == end:
                tpmax *= 2
                if tpmax > maxLen:
                    maxLen = tpmax
                    index = i

        i += 1

    return index, maxLen


if __name__ == '__main__':
    s = 'abbbbbacaabaaba'

    index, length = GetLong(s)
    print(index, length)
    print(s[index: index+length])











