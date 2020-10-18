import math

N = 1000

if __name__ == '__main__':
    f1 = [0] * (N + 1)
    f2 = [0] * (N + 1)
    f3 = [0] * (N + 1)

    # 一部
    for i in range(1, N+1):
        f1[i] = i

    # 2部
    for i in range(1, N+1):
        ans = math.inf
        for j in range(1, i+1):
            M = 1 + max(f2[i-j], f1[j-1])
            ans = min(ans, M)
        f2[i] = ans

    # 3部
    for i in range(1, N+1):
        ans = math.inf
        for j in range(1, i+1):
            M = 1 + max(f3[i-j], f2[j-1])
            ans = min(ans, M)
        f3[i] = ans

    print(f3[-1])