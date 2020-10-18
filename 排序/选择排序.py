from Array import RandArr

def selectSort(arr: list):
    length = len(arr)
    for i in range(length):
        minIndex = i
        for j in range(i+1, length):
            if arr[minIndex] > arr[j]:
                minIndex = j

        arr[minIndex], arr[i] = arr[i], arr[minIndex]
    return arr


if __name__ == '__main__':
    arr = RandArr(10)

    print(selectSort(arr))