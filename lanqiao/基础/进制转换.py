if __name__ == '__main__':
    n = int(input())
    List = [oct(int(input(), 16)) for _ in range(n)]
    for i in List:
        print(i[2:])

