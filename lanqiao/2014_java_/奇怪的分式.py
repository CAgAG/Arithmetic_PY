def f(a, b, c, d):
    return (a / b) * (c / d) == (a * 10 + c) / (b * 10 + d)


if __name__ == '__main__':
    count = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j: continue
            for a in range(1, 10):
                for b in range(1, 10):
                    if a == b: continue
                    if f(i, j, a, b):
                        count += 1
    print(count)
