# 哈希法
def Sort(arr: list):
    Map = dict()
    for e in arr:
        if Map.get(e) is None:
            Map[e] = 1
        else:
            Map[e] += 1

    Map = sorted(Map.items(), key=lambda x: x[0])

    for k, v in Map:
        i = 0
        while i < v:
            print(k, end=" ")
            i += 1
        print()

if __name__ == '__main__':
    arr = [
        1, 1, 3, 1, 4, 2, 2, 2, 2
    ]

    Sort(arr)



