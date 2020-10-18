import itertools


def checkIndex(x, y):
    if x >= 0 and x <= 2 and y >= 0 and y <= 3:
        return True
    return False


def dfs(x, y, Map: list):
    Map[x][y] = 0
    if checkIndex(x + 1, y) and Map[x + 1][y] == 1:
        dfs(x + 1, y, Map)
    if checkIndex(x - 1, y) and Map[x - 1][y] == 1:
        dfs(x - 1, y, Map)
    if checkIndex(x, y + 1) and Map[x][y + 1] == 1:
        dfs(x, y + 1, Map)
    if checkIndex(x, y - 1) and Map[x][y - 1] == 1:
        dfs(x, y - 1, Map)


def check(arr):
    # 构建arr 0-1 map
    count = 1
    Map = []
    for i in range(3):
        tp = []
        for j in range(4):
            if count in arr:
                tp.append(1)
            else:
                tp.append(0)
            count += 1
        Map.append(tp)

    count = 0
    for i in range(3):
        for j in range(4):
            if Map[i][j] == 1:
                dfs(i, j, Map)
                count += 1
    return count == 1


if __name__ == '__main__':
    # (1, 5, 7, 9, 11) 连通性检查
    count = 0
    for arr in itertools.combinations([i for i in range(1, 13)], 5):
        if check(arr):
            print(arr)
            count += 1
    print(count)
