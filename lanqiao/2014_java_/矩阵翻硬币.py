# 正面 偶数
# 反面 奇数

def getMaxi(n, m):
    List = [[]]
    for _ in range(n+1):
        List.append(
            [.5] + [0 for _ in range(m)]
        )
    return List


def op(List, x, y, n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            xpos = x * i
            ypos = y * j
            if xpos <= n and ypos <= m:
                List[xpos][ypos] += 1

def Q(n, m):
    arr = getMaxi(n, m)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j == 0:
                continue
            op(arr, i, j, n, m)

    count = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j == 0:
                continue
            ele = arr[i][j]
            if ele % 2 == 1 and isinstance(ele, int):
                count += 1
    return arr, count


if __name__ == '__main__':
    print(Q(2, 5))
