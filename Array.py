import random


def RandArr(num: int, low=-100, high=101):
    arr = []
    for i in range(num):
        arr.append(random.randint(low, high))
    print('随机列表:', arr)
    return arr


# 打乱数组
def ShuffleArr(arr: list):
    random.shuffle(arr)


# 随机重复数组
def RandRepeatArr(num: int):
    arr = RandArr(num // 2) * 2
    ShuffleArr(arr)
    return arr


# 交换
def Swap(arr, i1: int, i2: int):
    arr[i1], arr[i2] = arr[i2], arr[i1]


if __name__ == '__main__':
    print(RandRepeatArr(10))
