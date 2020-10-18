def f(r, n):
    return (1 + r) ** n


if __name__ == '__main__':
    for i in range(5):
        print(f(0.06, i+1))
