import math


def ipt():
    return [int(i) for i in input().strip().split(' ')]


arr = []
visited = []
m, n = 0, 0
total = 0
ans = math.inf


def dfs(i, j, steps, Sum):
    global ans
    if i < 0 or i == n or j < 0 or j == m \
            or visited[i][j] == 1:
        return

    if Sum == total // 2:
        ans = min(ans, steps)
        return
    # 剪枝
    elif Sum > total // 2:
        return

    # 标记
    visited[i][j] = 1
    dfs(i + 1, j, steps + 1, Sum + arr[i][j])
    dfs(i - 1, j, steps + 1, Sum + arr[i][j])
    dfs(i, j - 1, steps + 1, Sum + arr[i][j])
    dfs(i, j + 1, steps + 1, Sum + arr[i][j])
    # 回溯
    visited[i][j] = 0


if __name__ == '__main__':
    m, n = ipt()
    for _ in range(n):
        a = ipt()
        total += sum(a)
        arr.append(a)
        visited.append([None] * len(a))

    dfs(0, 0, 0, 0)
    print(ans)