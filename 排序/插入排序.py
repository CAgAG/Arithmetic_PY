from Array import RandArr


def InsertSort(arr: list):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    arr = RandArr(10)

    print(InsertSort(arr))
