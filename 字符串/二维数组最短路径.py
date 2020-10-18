"""
    左上角->右下角
    沿途整数之和最小
"""


# 倒着走
def GetMinPath(arr: list, i: int, j: int):
    # 原点
    if i == 0 and j == 0:
        return arr[i][j]
    # 选最小路径
    elif i > 0 and j > 0:
        return arr[i][j] + \
               min(GetMinPath(arr, i - 1, j), GetMinPath(arr, i, j - 1))
    # 特殊条件
    elif i > 0 and j == 0:
        return arr[i][j] + GetMinPath(arr, i - 1, j)
    else:
        return arr[i][j] + GetMinPath(arr, i, j - 1)


def GetMinPathI(arr: list):
    if arr is None or len(arr) == 0:
        return 0
    return GetMinPath(arr, len(arr) - 1, len(arr[0]) - 1)


# 动态规划
# 顺着走
def GetMinPathII(arr: list):
    if arr is None:
        return 0

    row = len(arr)
    col = len(arr[0])
    # 存储计算中间值
    cache = [[0] * col for i in range(row)]
    cache[0][0] = arr[0][0]
    # 第一行累加
    j = 0
    while j < col:
        cache[0][j] = cache[0][j - 1] + arr[0][j]
        j += 1
    # 第一列累加
    i = 1
    while i < row:
        cache[i][0] = cache[i - 1][0] + arr[i][0]
        i += 1

    i = 1
    while i < row:
        j = 1
        while j < col:
            if cache[i - 1][j] > cache[i][j - 1]:
                cache[i][j] = cache[i][j - 1] + arr[i][j]
            else:
                cache[i][j] = cache[i - 1][j] + arr[i][j]

            j += 1
        i += 1

    return cache[row - 1][col - 1]


if __name__ == '__main__':
    arr = [
        [1, 4, 3],
        [8, 7, 5],
        [2, 1, 5]
    ]

    print(GetMinPathII(arr))
