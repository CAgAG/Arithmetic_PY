def getStr():
    start = 97
    s = ''
    for i in range(19):
        s += chr(i + start)
    return s * 106


def build(arr: str):
    while len(arr) != 1:
        arr = arr[1::2]
    return arr


if __name__ == '__main__':
    print(build(getStr()))

    # arr = [
    #         i for i in range(10)
    #     ]
    # print(arr)
    # n = 3
    # # arr = arr[1:]
    # print(arr[::n-1])
