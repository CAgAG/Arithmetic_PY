import itertools


def check(arr):
    if (
            abs(arr[0] - arr[1]) == 1 or abs(arr[0] - arr[4]) == 1 or
            abs(arr[0] - arr[3]) == 1 or abs(arr[0] - arr[5]) == 1
    ):
        return False
    if (
            abs(arr[1] - arr[2]) == 1 or abs(arr[1] - arr[4]) == 1 or
            abs(arr[1] - arr[5]) == 1 or abs(arr[1] - arr[6]) == 1
    ):
        return False
    if (
            abs(arr[2] - arr[6]) == 1 or abs(arr[2] - arr[5]) == 1
    ):
        return False
    if (
            abs(arr[3] - arr[4]) == 1 or abs(arr[3] - arr[7]) == 1 or
            abs(arr[3] - arr[8]) == 1
    ):
        return False
    if (
            abs(arr[4] - arr[5]) == 1 or abs(arr[4] - arr[9]) == 1 or
            abs(arr[4] - arr[8]) == 1 or abs(arr[4] - arr[7]) == 1
    ):
        return False
    if (
            abs(arr[5] - arr[6]) == 1 or abs(arr[5] - arr[9]) == 1 or
            abs(arr[5] - arr[8]) == 1
    ):
        return False
    if (
            abs(arr[6] - arr[9]) == 1
    ):
        return False
    if (
            abs(arr[7] - arr[8]) == 1
    ):
        return False
    if (
            abs(arr[8] - arr[9]) == 1
    ):
        return False
    return True


if __name__ == '__main__':
    count = 0
    for arr in itertools.permutations([i for i in range(10)], 10):
        if check(arr):
            count += 1
    print(count)
