if __name__ == '__main__':
    num = int(input())
    arr = []
    for _ in range(num):
        arr += [int(i) for i in input().strip().split(' ')]
    arr.sort()
    s_num = 0
    n_num = 0
    for index in range(len(arr) - 1):
        if arr[index] == arr[index + 1]:
            s_num = arr[index]
        if arr[index + 1] - arr[index] == 2:
            n_num = arr[index] + 1

    print(n_num, s_num)
