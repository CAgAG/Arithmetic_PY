def f(num):
    if num == 1:
        return [[1]]
    if num == 2:
        return [[1], [1, 1]]
    L = [
        [1], [1, 1]
    ]

    for i in range(2, num):
        addNum = i - 1
        tp = [1]
        for j in range(1, addNum + 1):
            tp.append(L[i - 1][j] + L[i - 1][j - 1])
        tp.append(1)
        L.append(tp)
    return L


if __name__ == '__main__':
    num = int(input())
    for i in f(num):
        for j in i:
            print(j, end=' ')
        print()
