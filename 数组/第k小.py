from Array import RandArr


def FindSmallK(arr: list, low: int, high: int, k: int):
    if arr is None:
        return

    i = low
    j = high
    splitdata = arr[i]

    # 一趟快排
    while i < j:
        while i < j and arr[j] >= splitdata:
            j -= 1
        if i < j:
            arr[i] = arr[j]
            i += 1
        while i < j and arr[i] <= splitdata:
            i += 1
        if i < j:
            arr[j] = arr[i]
            j -= 1
    arr[i] = splitdata

    # splitdata 的下标偏移量
    subArrIndex = i - low
    if subArrIndex == k - 1:
        return arr[i]
    elif subArrIndex > k - 1:
        return FindSmallK(arr, low, i - 1, k)
    else:
        return FindSmallK(arr, i + 1, high, k - subArrIndex - 1)


# 变形
# 寻找top3
def FindTop3(arr: list):
    if arr is None:
        return

    top1 = top2 = top3 = -2 ** 32

    for v in arr:
        if v > top1:
            top3 = top2
            top2 = top1
            top1 = v
        elif v > top2 and v != top1:
            top3 = top2
            top2 = v
        elif v > top3 and v != top2:
            top3 = v

    print(top1, top2, top3)


if __name__ == '__main__':
    arr = RandArr(10)

    print(sorted(arr))
    print(FindSmallK(arr, 0, len(arr) - 1, 3))
    FindTop3(arr)
    print(arr)
