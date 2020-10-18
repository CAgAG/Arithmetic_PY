import itertools


def check(arr):
    for i in range(1, len(arr)-1, 2):
        if arr[i] >= arr[i-1] or arr[i+1] <= arr[i]:
            return False
    return True


m, n = input().strip().split(' ')
m, n = int(m), int(n)

num = 0
for i in itertools.product([i for i in range(1, n + 1)], repeat=m):
    if i[0] == 1:
        continue

    if check(i):
        # print(i)
        num += 1

print((num) % 10000)
