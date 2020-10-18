from Array import RandArr


def shellSort(arr: list):
    length = len(arr)
    step = 2
    group = length // step

    while group > 0:
        for i in range(group, length):
            key = arr[i]
            pre = i - group
            while pre >= 0 and arr[pre] > key:
                arr[pre + group] = arr[pre]
                pre -= group
            arr[pre + group] = key
        group //= step

    return arr


if __name__ == '__main__':
    arr = RandArr(10)

    print(shellSort(arr))