if __name__ == '__main__':
    n = int(input())
    count = 0
    while n >= 3:
        n -= 2
        count += 3
    count += n
    print(count)