def Permutation(arr: list, start: int):
    if arr is None or start < 0:
        return
    length = len(arr)
    if start == length - 1:
        return print(''.join(arr), end=" ")
    else:
        i = start
        while i < length:
            # 交换
            arr[i], arr[start] = arr[start], arr[i]
            # 固定一个字符, 对剩余字符进行全排列
            Permutation(arr, start + 1)
            # 还原
            arr[i], arr[start] = arr[start], arr[i]
            i += 1

# 变形
# 去除重复的排列
# [start..end) 区间是否有字符与 end位置的字符相同
def isDup(Str, start: int, end: int):
    i = start
    while i < end:
        if Str[i] == Str[end]:
            return False
        i += 1
    return True

def PermutationX(arr: list, start: int):
    if arr is None or start < 0:
        return
    length = len(arr)
    if start == length - 1:
        return print(''.join(arr), end=" ")
    else:
        i = start
        while i < length:
            if not isDup(arr, start, i):
                i += 1
                continue
            # 交换
            arr[i], arr[start] = arr[start], arr[i]
            # 固定一个字符, 对剩余字符进行全排列
            Permutation(arr, start + 1)
            # 还原
            arr[i], arr[start] = arr[start], arr[i]
            i += 1

if __name__ == '__main__':
    Str = '1231'
    PermutationX(list(Str), 0)
