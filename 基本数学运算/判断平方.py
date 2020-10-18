def isPow(n: int):
    low = 1
    high = n

    while low < high:
        mid = (low + high) // 2
        power = mid * mid
        if power > n:
            high = mid - 1
        elif power < low:
            low = mid + 1
        else:
            return True
    return False


# 数学推导
def isPower(n: int):
    minus = 1
    while n > 0:
        n -= minus
        if n == 0:
            return True
        elif n < 0:
            return False
        else:
            minus += 2
    return False


if __name__ == '__main__':
    print(isPower(13 ** 2))
