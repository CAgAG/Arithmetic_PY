def f(L, R):
    length = R - L + 1
    return L * length + length * (length - 1) // 2

if __name__ == '__main__':
    for i in range(2, 50):
        for j in range(i+2, 50):
            if f(1, i-1) + i*(i+1) + f(i+2, j-1) + j*(j+1) + f(j+2, 49) == 2015:
                print(i, j)
