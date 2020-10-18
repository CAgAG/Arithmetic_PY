n, m = input().strip().split(' ')
r, c = input().strip().split(' ')

m, n, r, c = int(n), int(m), int(r), int(c)

length = n * m
b = [i for i in range(1, length + 1)]
matrix = [[0 for _ in range(n)] for i in range(m)]

k = 0
i = 0
j = 0
left = 0
while k < length:
    while k < length and i < n - 1:
        matrix[j][i] = b[k]
        i += 1
        k += 1
    while k < length and j < m - 1:
        matrix[j][i] = b[k]
        j += 1
        k += 1
    while k < length and i > left:
        matrix[j][i] = b[k]
        i -= 1
        k += 1
    while k < length and j > left:
        matrix[j][i] = b[k]
        j -= 1
        k += 1
    i, j, left, m, n = i + 1, j + 1, left + 1, m - 1, n - 1
    # 考虑是矩阵时的情况
    if k == length - 1:
        matrix[j][i] = b[k]
        k += 1

for i in matrix:
    print(i)

print(matrix[r-1][c-1])










