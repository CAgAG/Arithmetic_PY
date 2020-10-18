if __name__ == '__main__':
    e = 1
    a = 9
    f = 0

    for b in range(2, 9):
        c = b + 1
        for g in range(2, 9):
            if b == g or g == c or c + g <= 10:
                continue
            if (c + g) % 10 == b:
                print(b, c, g)
            if ((c + g) % 10 + 1) == b:
                print('-->', b, c, g)
    """
    --> 2 3 8
    --> 3 4 8
    
    --> 4 5 8
    --> 5 6 8 --
    --> 6 7 8
    """
    # b = 2, 3, 4, 5, 6,
    # d+b>10 (d+b)%10==i
    for b in [2, 3, 4, 5, 6,]:
        for d in range(2, 9):
            if d+b <= 10 or d == b:
                continue
            for i in range(2, 9):
                if i == b or i == d or (d+b)%10!=i:
                    continue
                print(b, d, i)
    """
    4 8 2 -
    5 7 2 --
    5 8 3 -
    6 7 3 -
    6 8 4 -
    """
