from Array import RandArr


# 动态规划
def MaxSubArr(arr: list):
    if arr is None:
        return

    length = len(arr)
    end = [None] * length
    all = [None] * length

    end[length - 1] = all[length - 1] = arr[length - 1]
    end[0] = all[0] = arr[0]

    i = 1
    while i < length:
        end[i] = max(end[i - 1] + arr[i], arr[i])
        all[i] = max(end[i], all[i - 1])
        i += 1
    return all[length - 1]

# 优化动态规划
def MaxSubArrPlus(arr: list):
    if arr is None:
        return

    length = len(arr)
    # 遍历连续最大值
    end = arr[0]
    # 记录
    all = arr[0]

    i = 1
    while i < length:
        end = max(end + arr[i], arr[i])
        all = max(end, all)
        i += 1
    return all

# 变形
# 最大连续值的位置
def MaxSubArrIndex(arr: list):
    if arr is None:
        return

    length = len(arr)
    # 遍历连续最大值
    end = arr[0]
    # 记录
    all = arr[0]

    Ibegin = 0
    Iend = 0

    i = 1
    while i < length:
        if end + arr[i] > arr[i]:
            end += arr[i]
        else:
            Ibegin = i
            end = arr[i]

        if end > all:
            Iend = i
            all = end
        i += 1
    return Ibegin, Iend



if __name__ == '__main__':
    arr = RandArr(10)

    print(MaxSubArrPlus(arr))
    print(MaxSubArrIndex(arr))
