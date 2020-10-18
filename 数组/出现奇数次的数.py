def GetNum(arr: list):
    if arr is None:
        return

    dic = dict()
    for v in arr:
        if dic.get(v) is None:
            dic[v] = 1
        else:
            dic[v] += 1

    for v, num in dic.items():
        if num % 2 != 0:
            print(v, end=" ")


# 异或: 任何一个数字, 异或自己其结果为0
#       反过来说, 任何数字异或0为自己本身
# def GetNumXOR(arr: list):
#     if arr is None:
#         return
#
#     length = len(arr)
#     result = 0
#     position = 0
#     # 循环一遍
#     i = 0
#     while i < length:
#         result ^= arr[i]
#         i += 1
#     # 临时保存结果
#     tp = result
#     # 找出异或结果中位值为1的位数
#     i = result
#     while i & 1 == 0:
#         position += 1
#         i >>= 1
#
#     i = 1
#     while i < length:
#         if ((arr[i] >> position) & 1) == 1:
#             result ^= arr[i]
#     return result ^ tp


if __name__ == '__main__':
    arr = [i for i in range(10)] * 2
    arr.append(3)
    arr.append(7)

    GetNum(arr)
    print(GetNum(arr))