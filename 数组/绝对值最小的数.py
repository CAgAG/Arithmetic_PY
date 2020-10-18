"""
    列表为升序
"""


def FindMin(arr: list):
    if arr is None:
        return

    length = len(arr)
    if arr[0] >= 0:
        return arr[0]
    if arr[length - 1] <= 0:
        return arr[length - 1]

    begin = 0
    end = length - 1

    # 找到正负分界点
    while True:
        mid = (begin + end) // 2
        if arr[mid] == 0:
            return 0
        elif arr[mid] > 0:
            if arr[mid - 1] > 0:
                end = mid - 1
            if arr[mid - 1] == 0:
                return 0
            else:
                break
        else:
            if arr[mid + 1] < 0:
                begin = mid + 1
            if arr[mid + 1] == 0:
                return 0
            else:
                break

    if arr[mid] > 0:
        if arr[mid] > abs(arr[mid - 1]):
            return abs(arr[mid - 1])
        else:
            return arr[mid]
    else:
        if abs(arr[mid]) > arr[mid + 1]:
            return arr[mid + 1]
        else:
            return arr[mid]


if __name__ == '__main__':
    arr = [
        -25, -10, -2, 1, 3, 98, 76
    ]

    print(FindMin(arr))
