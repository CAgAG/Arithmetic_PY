def power(d: int, n: int):
    if n == 0: return 1
    if n == 1: return d

    tp = power(d, abs(n) // 2)

    if n > 0:
        # 奇数
        if n % 2 == 1:
            return tp * tp * d  # +1
        else:
            return tp * tp
    else:
        if n % 2 == 1:
            return 1 / (tp * tp * d)
        else:
            return 1 / (tp * tp)


if __name__ == '__main__':
    print(power(3, 4))
