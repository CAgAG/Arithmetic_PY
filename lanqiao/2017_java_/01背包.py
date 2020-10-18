N = 5 + 1
W = 20 + 1

"""
    列: 背包最大重量
    行: 最多可拿的价值
"""
B = [
    [0] * W for _ in range(N)
]
# 重量
w = [
    0,
    2, 3, 4, 5, 9
]
# 价值
v = [
    0,
    3, 4, 5, 8, 10
]


def knapsack():
    for k in range(1, N):
        # c代表背包最大重量
        for c in range(1, W):
            if w[k] > c:
                B[k][c] = B[k - 1][c]
            else:
                v1 = B[k - 1][c - w[k]] + v[k]
                v2 = B[k - 1][c]
                if v1 > v2:
                    B[k][c] = v1
                else:
                    B[k][c] = v2


if __name__ == '__main__':
    knapsack()
    # print(B)
    print(B[-1][-1])