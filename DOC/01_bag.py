
if __name__ == '__main__':
    # 背包空间
    space = 10
    # 默认第一个元素为 0, 仅仅是为了方便理解
    weights = [0, 2, 2, 3, 1, 5, 2]
    values = [0, 2, 3, 1, 5, 4, 3]

    n = len(values)

    # 初始化全为0, 但输出结果仅第一行和第一列均为 0
    maxitr = [[0 for _ in range(space + 1)] for _ in range(n)]

    for i in range(1, n):
        # 当前物品的重量和价值
        weight = weights[i]
        value = values[i]
        for j in range(1, space + 1):  # 第0个默认为 0
            # 上一次的最大价值
            last_max_value = maxitr[i - 1][j]

            # 如果还可以装下
            if j >= weight:
                """
                这是为了j - weight >= 0, 不出现索引错误
                真正的判断是 maxitr[][j - weight]: 得到的是刚好满足当前重量的背包容量的最大价值
                """
                maxitr[i][j] = max(last_max_value, maxitr[i - 1][j - weight] + value)
            else:
                maxitr[i][j] = last_max_value

    for data in maxitr:
        print(data)










