"""
    数组含有重复元素
"""


# 动态规划
def MinDistance(arr: list, num1: int, num2: int):
    if arr is None:
        return

    length = len(arr)
    lastPos1 = lastPos2 = -1
    minDis = length

    i = 0
    while i < length:
        if arr[i] == num1:
            lastPos1 = i
            if lastPos2 >= 0:
                minDis = min(minDis, lastPos1 - lastPos2)
        if arr[i] == num2:
            lastPos2 = i
            if lastPos1 >= 0:
                minDis = min(minDis, lastPos2 - lastPos1)
        i += 1

    return minDis


if __name__ == '__main__':
    arr = [
        i for i in range(10)
    ]
    arr.append(5)
    arr.insert(2, 8)

    print(arr)
    print(MinDistance(arr, 5, 8))
