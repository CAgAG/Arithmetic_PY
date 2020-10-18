arr = []
if __name__ == '__main__':
    factor = 2 ** 30
    for i in range(29):
        tp = input().strip().split(' ')
        tp = [int(i) * factor for i in tp]
        arr.append(tp)
    arr.append([0]*30)

    for i in range(29):
        for j in range(i+1):
            half = arr[i][j] // 2
            arr[i+1][j] += half
            arr[i+1][j+1] += half

    print(min(arr[-1]))
    print(max(arr[-1]))
