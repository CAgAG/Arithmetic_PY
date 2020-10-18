def check(arr: list):
    pivot = arr[0]
    if pivot % 2 != 0:
        return False
    for i in arr[1:]:
        if i != pivot:
            return False
    return True


def op(arr: list, length: int):
    tp = []
    for i in range(length):
        arr[i] //= 2
        tp.append(arr[i])
    num = tp[0]
    tp = tp[1:]
    tp.append(num)
    for a in range(length):
        arr[a] += tp[a]


def build(num: int, circle: list):
    count = 0
    while True:
        op(circle, num)
        if check(circle):
            return count
        else:
            for index, v in enumerate(circle):
                if v % 2 != 0:
                    circle[index] += 1
                    count += 1


if __name__ == '__main__':
    print(build(3, [2, 2, 4]))

    # arr = [2, 2, 4]
    # op(arr, len(arr))
    # print(arr)
