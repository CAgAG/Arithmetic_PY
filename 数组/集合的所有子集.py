# 位图法
def GetAllSubSet(arr: list, mask: list, c: int):
    length = len(arr)
    if length == c:
        i = 0
        while i < length:
            if mask[i] == 1:
                print(arr[i], end=" ")
            i += 1
        print()
    else:
        mask[c] = 1
        GetAllSubSet(arr, mask, c + 1)
        mask[c] = 0
        GetAllSubSet(arr, mask, c + 1)


# 迭代法
def GetAllSubSetX(Str: str):
    if str is None:
        return
    arr = [Str[0]]
    i = 1
    while i < len(Str):
        length = len(arr)
        j = 0
        while j < length:
            arr.append(arr[j] + Str[i])
            j += 1
        arr.append(Str[i])
        i += 1

    print(arr)


if __name__ == '__main__':
    arr = ['a', 'b', 'c']
    mask = [0] * 3
    # GetAllSubSet(arr, mask, 0)
    GetAllSubSetX(''.join(arr))
