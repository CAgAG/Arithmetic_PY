# 整数快速幂
def quick(a, n):
    ans = 1
    while n:
        if n % 2 != 0:
            ans *= a % mod
        a *= a % mod
        n >>= 1
    return ans % mod


if __name__ == '__main__':
    a, b, n = map(int, input().split())
    mod = b * 1000

    s = quick(10, n + 2)

    print(a * s % mod // b)
