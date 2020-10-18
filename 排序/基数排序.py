from Array import RandArr


def radixSort(arr: list):
    maxEle = max(arr)
    # 最大值有几位
    maxDigit = 0
    while maxEle != 0:
        maxEle //= 10
        maxDigit += 1

    mod = 10
    div = 1
    bucket = [[] for _ in range(10)]

    for i in range(maxDigit):
        for j in range(len(arr)):
            num = arr[j] % mod // div
            bucket[num].append(arr[j])

        # 回填
        arr.clear()
        for j in range(10):
            arr += bucket[j]
            bucket[j].clear()

        i += 1
        mod *= 10
        div *= 10

    return arr


if __name__ == '__main__':
    arr = RandArr(10, low=0, high=1000)

    print(radixSort(arr))
