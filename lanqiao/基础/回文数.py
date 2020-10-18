# if __name__ == '__main__':
#     for i in range(1001, 10000):
#         si = str(i)
#         if si[:2] == si[:1:-1]:
#             print(si)

if __name__ == '__main__':
    for i in range(100, 1000):
        o = i // 100
        th = i % 10
        tw = i // 10 % 10
        if o**3 + th**3 + tw**3 == i:
            print(i)
