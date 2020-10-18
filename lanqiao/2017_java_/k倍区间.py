if __name__ == '__main__':
    num, k = input().strip().split(' ')
    num, k = int(num), int(k)

    SNum = [0]
    for i in range(1, num + 1):
        n = int(input())
        SNum.append(
            SNum[i - 1] + n
        )
    ans = 0
    for i in range(1, num + 1):
        for j in range(i, num + 1):
            if (SNum[j] - SNum[i - 1]) % k == 0:
                ans += 1

    print(ans)
