# 空间换时间
def findDup(arr: list):
    if arr is None:
        return -1

    dic = dict()
    for i, v in enumerate(arr):
        if dic.get(v) == None:
            dic[v] = 0
        else:
            return v


def findDupAdd(arr: list):
    if arr is None:
        return -1
    return sum(arr) - sum(set(arr))


# 异或法
def findDupXOR(arr: list):
    if arr is None:
        return -1
    result = 0
    for i in arr:
        result ^= i
        result ^= 1
    return result


if __name__ == '__main__':
    arr = [i for i in range(10)]
    arr.append(5)

    print(findDupAdd(arr))
