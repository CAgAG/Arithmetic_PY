"""
    假设列表升序
"""


def FindCommon(arr1: list, arr2: list, arr3: list):
    i = j = k = 0
    L1 = len(arr1)
    L2 = len(arr2)
    L3 = len(arr3)

    while i < L1 and j < L2 and k < L3:
        if arr1[i] == arr2[j] == arr3[k]:
            print(arr1[i], end=" ")
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1


if __name__ == '__main__':
    arr1 = [i for i in range(10)]
    arr2 = [i for i in range(5, 16)]
    arr3 = [i for i in range(7, 12)]

    FindCommon(arr1, arr2, arr3)
