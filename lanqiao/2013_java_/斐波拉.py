import decimal

if __name__ == '__main__':
    decimal.getcontext().prec = 100
    a = decimal.Decimal(1)
    b = decimal.Decimal(1)
    for i in range(500):
        t = b
        b += a
        a = t
    print(a/b)


