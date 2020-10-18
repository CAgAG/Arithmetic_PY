from Array import RandArr


# 合并两个有序数组
def merge(a: list, b: list):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1

    result += a[i:]
    result += b[j:]
    return result


def mergeSort(arr: list):
    length = len(arr)
    if length <= 1:
        return arr

    mid = length // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


if __name__ == '__main__':
    arr = RandArr(10)

    print(mergeSort(arr))
