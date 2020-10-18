from Array import RandArr


def bubbleSort(arr: list):
    length = len(arr)
    for i in range(length-1):
        flag = True
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
        if flag:
            break

    return arr


if __name__ == '__main__':
    arr = RandArr(10)

    print(bubbleSort(arr))