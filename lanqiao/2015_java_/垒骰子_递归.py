MOD = 10 ** 9 + 7
# 规则映射
op = [-1] * 7
# 冲突
conflict = [[False for _ in range(7)] for _ in range(7)]


def init():
    op[1] = 4
    op[4] = 1
    op[2] = 5
    op[5] = 2
    op[3] = 6
    op[6] = 3


def f(up, n):
    """
    :param up: 那个面朝上
    :param n: 第几个骰子
    :return:
    """
    if n == 0:
        return 4

    ans = 0
    for upp in range(1, 7):
        if conflict[op[up]][upp]:
            continue
        ans = (ans + f(upp, n - 1)) % MOD
    return ans


if __name__ == '__main__':
    n, m = input().strip().split(' ')
    n = int(n)

    for i in range(int(m)):
        x, y = input().strip().split(' ')
        conflict[int(x)][int(y)] = True
        conflict[int(y)][int(x)] = True

    ans = 0
    for up in range(1, 7):
        ans = (ans + 4 * f(up, n - 1)) % MOD
    print(ans)

    
