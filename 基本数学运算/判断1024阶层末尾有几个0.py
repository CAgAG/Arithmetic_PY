# 因子法
# 5 与任何一个偶数相乘都会增加末尾0的个数
def zeroCount(n: int):
    count = 0
    while n > 0:
        n /= 5
        count += n
    return round(count)


# 变形
# N! -> N/5 + N/5**2 + n/5*3 ... + N/5**m   (5**m < N and 5**(m+1) > N)

if __name__ == '__main__':
    print(zeroCount(1024))

    a = 5
    b = 6