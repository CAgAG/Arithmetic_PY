N = 4  # 边界


def isSafe(Map: list, x: int, y: int):
    return x >= 0 and x < N and y >= 0 and y < N and Map[x][y] == 1


def GetPath(Map: list, x: int, y: int, sol: list):
    # 到达边界, goal
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    if isSafe(Map, x, y):
        # 标记当前单元为可移动
        sol[x][y] = 1
        # 右走一步
        if GetPath(Map, x + 1, y, sol):
            return True
        # 下走一步
        if GetPath(Map, x, y + 1, sol):
            return True
        # 回溯
        sol[x][y] = 0
    return False


if __name__ == '__main__':
    Map = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

    sol = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    if GetPath(Map, 0, 0, sol):
        print('到达')
