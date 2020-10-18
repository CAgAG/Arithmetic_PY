"""
    数组值为 原点到指定点的长度
"""
def MaxCover(arr: list, L: int):
    count = 2
    # 最长覆盖的点数
    maxCount = 1
    length = len(arr)
    # 覆盖点开始位置
    start = 0
    # 假设开始位置
    i = 0
    # 假设结束位置
    j = 1

    while i < length and j < length:
        while j < length and (arr[j] - arr[i] <= L):
            j += 1
            count += 1
        j -= 1
        count -= 1

        if count > maxCount:
            start = i
            maxCount = count

        i += 1
        j += 1

    return start, maxCount


if __name__ == '__main__':
    arr = [
        1, 3, 7, 8, 10, 11, 12, 15, 17, 19, 22
    ]

    start, length = MaxCover(arr, 8)
    print(start, length, arr[start: start+length])

