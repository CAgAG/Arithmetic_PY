if __name__ == '__main__':
    cnum, pnum = input().strip().split(' ')
    cnum, pnum = int(cnum), int(pnum)

    area = []
    Min = 100001

    for _ in range(cnum):
        a, b = input().strip().split(' ')
        a = int(a)
        b = int(b)
        area.append(a * b)
        if a < Min:
            Min = a
        if b < Min:
            Min = b
    left = 1
    right = Min + 1
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(cnum):
            cnt += area[i] // mid ** 2

        if cnt >= pnum:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    print(ans)
