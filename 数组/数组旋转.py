"""
    二维数组逆时针旋转45°
"""


def RotateArr(arr: list):
    length = len(arr)

    # 右上部分, 不含对角线
    i = length - 1
    while i > 0:
        row = 0
        col = i
        while col < length:
            print(arr[row][col], end=" ")
            row += 1
            col += 1
        print()
        i -= 1

    # 打印左下部分, 含对角线
    i = 0
    while i < length:
        row = i
        col = 0
        while row < length:
            print(arr[row][col], end=" ")
            row += 1
            col += 1
        print()
        i += 1


if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    RotateArr(arr)
