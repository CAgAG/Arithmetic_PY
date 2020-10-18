"""
    假设数据整体升序
"""
import bisect


def FindWithBinary(arr: list, data: int):
    if arr is None:
        return False

    i = 0

    rows = len(arr)
    col = len(arr[0])

    j = col - 1
    # 从右上角开始
    while i < rows and j >= 0:
        if arr[i][j] == data:
            return True
        elif arr[i][j] > data:
            # 横向移动
            j -= 1
        else:
            # 纵向移动
            i += 1


if __name__ == '__main__':
    arr = [
        [i for i in range(3)],
        [i for i in range(5, 8)],
        [i for i in range(10, 13)]
    ]

    print(FindWithBinary(arr, 12))
