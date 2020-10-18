"""
    和 等于整数的组合, 递增
"""


def GetAllComb(n: int):
    j = 1
    result = []
    while j <= n // 2:
        length = n // j
        arr = [j] * length

        i = 0
        while i < length - 1:
            sums = sum(arr)
            while sums <= n:
                if sums == n:
                    result.append(arr[:])
                arr[-1] += 1
                sums = sum(arr)

            arr.pop()
            i += 1
        j += 1
    result.append([n])
    return result


if __name__ == '__main__':
    print(GetAllComb(7))
