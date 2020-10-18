def find(L, pivot, length):
    for i in range(length):
        if L[i] == pivot:
            return int(i) + 1
    return -1

if __name__ == '__main__':
    length = int(input())
    L = input().split(' ')
    pivot = input()
    print(find(L, pivot, length))
