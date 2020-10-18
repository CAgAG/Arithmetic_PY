from Array import RandArr


def adjustHeap(arr: list, index: int, size: int):
    lchild = 2 * index + 1
    rchild = 2 * index + 2

    maxIndex = index

    if index < size // 2:
        if lchild < size and arr[lchild] > arr[maxIndex]:
            maxIndex = lchild
        if rchild < size and arr[rchild] > arr[maxIndex]:
            maxIndex = rchild
        if maxIndex != index:
            arr[maxIndex], arr[index] = arr[index], arr[maxIndex]
            adjustHeap(arr, maxIndex, size)


def buildHeap(arr: list, size: int):
    for i in range(size // 2)[::-1]:
        adjustHeap(arr, i, size)


def heapSort(arr: list):
    length = len(arr)
    buildHeap(arr, length)
    for i in range(length)[::-1]:
        arr[0], arr[i] = arr[i], arr[0]
        adjustHeap(arr, 0, i)

    return arr


if __name__ == '__main__':
    arr = RandArr(10)

    print(heapSort(arr))
