# 重复偶数次
def FindSingle(arr: list):
    res = 0
    for v in arr:
        res ^= v
    return res


if __name__ == '__main__':
    arr = [
        i for i in range(10)
    ] * 4
    arr.append(10)

    print(FindSingle(arr))
