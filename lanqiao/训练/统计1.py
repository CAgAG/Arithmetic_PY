if __name__ == '__main__':
    L, R = input().strip().split(' ')
    count = 0
    for i in range(int(L), int(R)+1):
        count += bin(i).count('1')
    print(count)