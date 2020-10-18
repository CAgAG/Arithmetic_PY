from Array import RandArr


def _GetMin(arr: list, low: int, high: int):
    # 旋转个数为0
    if high < low:
        return arr[0]
    # 只有一个元素
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    # 判断arr[mid] 是否为最小值
    if arr[mid] < arr[mid-1]:
        return arr[mid]
    # 判断arr[mid+1] 是否为最小值
    elif arr[mid+1] < arr[mid]:
        return arr[mid+1]
    # 在左半部分
    elif arr[high] > arr[mid]:
        return _GetMin(arr, low, mid-1)
    # 在右半部分
    elif arr[mid] > arr[low]:
        return _GetMin(arr, mid+1, high)
    else:
        return min(_GetMin(arr, low, mid-1), _GetMin(arr, mid+1, high))

def GetMin(arr: list):
    if arr is None:
        return
    return _GetMin(arr, 0, len(arr)-1)


# 旋转数组
def RotateArr(arr: list, split: int):
    for i in range(split):
        arr.insert(0, arr.pop())


if __name__ == '__main__':
    arr = [i for i in range(10)]
    RotateArr(arr, 2)
    print(arr)

    print(GetMin(arr))















