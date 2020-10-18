def Edit(s1: str, s2: str, wight: int):
    if (s1 or s2) is None:
        return 0
    if s1 is None:
        return len(s2)
    if s2 is None:
        return len(s1)

    length_1 = len(s1)
    length_2 = len(s2)

    # 中间计算结果, 二维数组
    """
        行: s2
        列: s1
    """
    Process = [
        [-1]*(length_2+1) for i in range(length_1 + 1)
    ]

    # 行首元素
    i = 0
    while i < length_1 + 1:
        Process[i][0] = i
        i += 1

    # 第一列
    i = 0
    while i < length_2 + 1:
        Process[0][i] = i
        i += 1

    i = 1
    while i < length_1 + 1:
        j = 1
        while j < length_2 + 1:
            # 找到最好方案
            # 删除, 添加, 替换
            if s1[i-1] == s2[j-1]:
                Process[i][j] = min(Process[i-1][j]+1, Process[i][j-1]+1, Process[i-1][j-1])
            else:
                Process[i][j] = min(Process[i-1][j]+1, Process[i][j-1]+1, Process[i-1][j-1]+wight)

            j += 1
        i += 1

    return Process[length_1][length_2]

if __name__ == '__main__':
    s1 = 'bciln'
    s2 = 'fciling'

    print(Edit(s1, s2, 1))



