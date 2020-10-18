def fob(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    arr = [1, 1]
    for _ in range(num - 2):
        arr[0], arr[1] = arr[1], (arr[0] + arr[1]) % 10007
    return arr[1]


if __name__ == '__main__':
    num = int(input())
    print(fob(num))
