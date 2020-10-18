if __name__ == '__main__':
    num = int(input())
    for i in range(10001, 100000):
        si = str(i)
        if si[:2] == si[:2:-1]:
            Sum = 0
            for i in si:
                Sum += int(i)
            if Sum == num:
                print(si)
    for i in range(100001, 1000000):
        si = str(i)

        if si[:3] == si[:2:-1]:
            Sum = 0
            for i in si:
                Sum += int(i)
            if Sum == num:
                print(si)

# if __name__ == '__main__':
#     # 898999
#     si = '898999'
#     print(si[:3], si[:1:-1])
