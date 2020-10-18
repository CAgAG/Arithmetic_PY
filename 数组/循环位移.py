from Array import RandArr


# 蛮力法
def RightShift(arr: list, k: int):
    for _ in range(k):
        arr.insert(0, arr.pop())


# 优化
def RightShiftX(arr: list, k: int):
    if arr is None:
        return

    k %= len(arr)

    if k != 0:
        RightShift(arr, k)


# 翻转法
def Reverse(arr: list, start: int, end: int):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def RightShiftXX(arr: list, k: int):
    if arr is None:
        return

    length = len(arr)
    k %= length
    # 左边先翻转
    Reverse(arr, 0, length - k - 1)
    # 右边翻转
    Reverse(arr, length - k, length - 1)
    # 整体翻转
    arr.reverse()


if __name__ == '__main__':
    arr = RandArr(10)
    RightShiftXX(arr, 3)
    print(arr)
