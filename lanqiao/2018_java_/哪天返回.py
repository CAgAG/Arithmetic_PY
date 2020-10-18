if __name__ == '__main__':
    money = 1
    Sm = 0
    day = 0
    while Sm < 108:
        Sm += money
        money += 2
        day += 1
    print(day)
