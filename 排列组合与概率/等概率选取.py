import random


# n: 选几个
def GetRand(arr: list, n: int):
    i = 0
    length = len(arr)
    while i < length:
        j = random.randint(i, length - 1)
        arr[i], arr[j] = arr[j], arr[i]
        i += 1


if __name__ == '__main__':
    arr = [
        i for i in range(10)
    ]
    n = 6
    GetRand(arr, n)
    print(arr[:n])
