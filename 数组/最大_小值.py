from Array import RandArr


def GetMaxMin(arr: list, left: int, right: int):
    if arr is None:
        return

    list = []
    mid = (left + right) // 2

    # left 和 right 之间只有一个元素
    if left == right:
        list.append(arr[left])
        list.append(arr[left])
        return list
    # left 和 right 之间只有2个元素
    if left + 1 == right:
        if arr[left] > arr[right]:
            Max = arr[left]
            Min = arr[right]
        else:
            Max = arr[right]
            Min = arr[left]
        list.append(Min)
        list.append(Max)
        return list

    LeftList = GetMaxMin(arr, left, mid)
    RightList = GetMaxMin(arr, mid+1, right)

    Max = LeftList[1] if LeftList[1]>RightList[1] else RightList[1]
    Min = LeftList[0] if LeftList[0]<RightList[0] else RightList[0]
    list.append(Min)
    list.append(Max)
    return list


if __name__ == '__main__':
    arr = RandArr(10)
    Min, Max_distance = GetMaxMin(arr, 0, len(arr) - 1)

    print(Max_distance, max(arr))
    print(Min, min(arr))


