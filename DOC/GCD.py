# 最大公约数
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


# 最小公倍数
def lcm(a, b):
    return a // gcd(a, b) * b

if __name__ == '__main__':
    a, b = 12, 12

    print(gcd(a, b))
    print(lcm(a, b))


