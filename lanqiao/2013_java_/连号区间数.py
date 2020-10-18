def f(start, length):
    return start * length + length * (length - 1) / 2


def check(arr: list):
    sortArr = sorted(arr)
    for i in range(len(sortArr) - 1):
        if sortArr[i + 1] - sortArr[i] != 1:
            return False
    return True


def build(arr: list):
    length = len(arr)
    count = 0
    for i in range(length):
        for j in range(i, length):
            if i == j:
                # print(i + 1, j + 1)
                count += 1
                continue
            if check(arr[i: j + 1]):
                # print(i + 1, j + 1)
                count += 1
    return count


if __name__ == '__main__':
    arr = [
        3, 4, 2, 5, 1
    ]
    print(build(arr))
