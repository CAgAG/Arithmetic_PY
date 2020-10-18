from Array import RandArr


def _quickSort(arr: list, left: int, right: int):
    if left >= right:
        return arr

    # 基准值
    key = arr[left]
    low = left
    high = right

    while left < right:
        # 找到右边小于key的位置
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]
        # 找到左边大于key的位置
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]

    # 此时left == right
    arr[left] = key

    _quickSort(arr, low, left - 1)
    _quickSort(arr, left + 1, high)
    return arr


def quickSort(arr: list):
    if arr is None:
        return None
    return _quickSort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = RandArr(10)

    print(quickSort(arr))
