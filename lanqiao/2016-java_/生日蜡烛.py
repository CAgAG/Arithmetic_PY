def f(start, end):
    length = end - start
    return start * length + length * (length - 1) // 2

if __name__ == '__main__':
    for i in range(1, 100):
        for j in range(i + 1, 100):
            if f(i, j) == 236:
                print(i)
                break



