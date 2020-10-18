def f(n):
    Map = {}
    c = 0
    while c ** 2 <= n // 2:
        d = c
        while pow(c, 2) + pow(d, 2) <= n:
            if Map.get(pow(c, 2)+pow(d, 2)) is None:
                Map[pow(c, 2)+pow(d, 2)] = c
            d += 1
        c += 1

    a = 0
    while pow(a, 2) <= n // 4:
        b = a
        while pow(b, 2) + pow(a, 2) <= n // 2:
            if Map.get(n - pow(a, 2) - pow(b, 2)) is not None:
                c = Map.get(n - pow(a, 2) - pow(b, 2))
                d = int(pow((n - pow(a, 2) - pow(b, 2) - pow(c, 2)), 0.5))
                print(a, b, c, d)
                return
            b += 1
        a += 1


if __name__ == '__main__':
    n = int(input())
    f(n)
