def Max(a: int, b: int):
    return ((a + b) + abs(a - b)) / 2


if __name__ == '__main__':
    a = 5
    b = 6

    print(Max_distance(b, a))
