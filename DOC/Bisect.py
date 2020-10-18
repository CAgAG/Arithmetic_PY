"""
     用于有序序列, 二分查找, 插入
"""
import bisect


# 快速实现二分查找
def BinSearch(arr, data):
    pivot = bisect.bisect_left(arr, data)
    if pivot == len(arr) or arr[pivot] != data:
        return -1
    return pivot


if __name__ == '__main__':
    arr = [
        i for i in range(10)
    ]
    arr.append(9)
    """
        不会查找失败
    """
    # 左边查找
    bisect.bisect_left(arr, 9)
    # 值相同的话, 左边插入
    bisect.insort_left(arr, 5.5)
    print(arr)
    # 右边查找
    bisect.bisect_right(arr, 9)
    # 值相同的话, 右边插入
    bisect.insort_right(arr, 5.6)
    print(arr)

    print(BinSearch(arr, 5.55))
