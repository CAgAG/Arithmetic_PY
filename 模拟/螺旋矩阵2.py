m, n = 4, 4

ALL = m*n
arr = [
    i for i in range(1, ALL+1)
]

maxi = [
    [0]*n for _ in range(m)
]

right = n - 1
left = 0
top = 0
bottom = m - 1

index = 0
while index < ALL:
    for i in range(left, right):
        maxi[top][i] = arr[index]
        index += 1

    for i in range(top, bottom):
        maxi[i][right] = arr[index]
        index += 1

    for i in range(right, left, -1):
        maxi[bottom][i] = arr[index]
        index += 1

    for i in range(bottom, top, -1):
        maxi[i][left] = arr[index]
        index += 1

    top += 1
    right -= 1
    left += 1
    bottom -= 1

for i in range(m):
    print(maxi[i])







