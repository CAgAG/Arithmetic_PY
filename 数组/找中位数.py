from Array import RandArr

# 一趟快排
# 以arr[low] 为基准, 分为两部分
def Partition(arr: list, low: int, high: int):
    key = arr[low]
    while low < high:
        while low < high and arr[high] > key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < key:
            low += 1
        arr[high] = arr[low]

    arr[low] = key
    return low


def GetMid(arr: list):
    low = 0
    length = len(arr)
    high = length - 1
    mid = (low + high) // 2

    while True:
        pivot = Partition(arr, low, high)
        # 找到
        if pivot == mid:
            break
        # 右半部分
        elif pivot > mid:
            high = pivot - 1
        # 左半部分
        else:
            low = pivot + 1

    # 奇偶, 中位数
    return arr[mid] if length % 2 != 0 else (arr[mid] + arr[mid + 1]) / 2


if __name__ == '__main__':
    arr = RandArr(9)
    print(GetMid(arr))