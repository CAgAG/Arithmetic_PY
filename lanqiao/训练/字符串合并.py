def swap(x, y):
    return y, x

if __name__ == '__main__':
    # print(input(), end='')
    # print(input())

    # x, y = input().strip().split(' ')
    # print(swap(x, y))

    input()
    arr = input().strip().split(' ')
    arr.sort(key=lambda x: int(x), reverse=True)
    print(' '.join(arr))

