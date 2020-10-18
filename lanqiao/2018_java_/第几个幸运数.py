def nthUglyNumber(n: int) -> int:
    p3, p5, p7 = 0, 0, 0
    rec = [1]
    while True:
        ugly = min(rec[p3] * 3, rec[p5] * 5, rec[p7] * 7)
        rec.append(ugly)

        if ugly >= n:
            break

        if ugly == rec[p3] * 3:
            p3 += 1
        if ugly == rec[p5] * 5:
            p5 += 1
        if ugly == rec[p7] * 7:
            p7 += 1

    return len(rec) - 1





if __name__ == '__main__':
    num = 59084709587505
    print(nthUglyNumber(num))

