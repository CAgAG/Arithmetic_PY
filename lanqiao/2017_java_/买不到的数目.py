"""
    ax+by=C，不定方程的解a=4，b=7，C=17 这种情况下，xy实际上有解，7*2+（7-4）==3*7-1*4
    a，b互质，一定有解且解的数目无穷
                ==
    C是gcd（a，b）的倍数，方程一定有解，而且有无穷多解
    条件：一定有解 -> a，b互质
    条件2：xy都是大于等于0的整数，在这个限定条件下有的C是无解的，那么C的上界是多少呢？至多是a*b
"""
if __name__ == '__main__':
    a, b = input().strip().split(' ')
    a, b = int(a), int(b)

    # 符合条件
    result = set()

    x = 0
    while a*x <= a*b:
        y = 0
        while a*x+b*y <= a*b:
            result.add(a*x+b*y)
            y += 1
        x += 1

    for v in range(a*b, -1, -1):
        if v not in result:
            print(v)
            break
    print(result)