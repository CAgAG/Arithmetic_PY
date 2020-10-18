
if __name__ == '__main__':
    space = 10
    # 直接第一个元素为 0
    weights = [0, 2, 2, 3, 1, 5, 2]
    values = [0, 2, 3, 1, 5, 4, 3]

    n = len(values)

    maxitr = [0 for _ in range(space + 1)]

    for i in range(1, n):
        # 当前物品的重量和价值
        weight = weights[i]
        value = values[i]
        for j in range(space, 0, -1):
            # 上一次的最大价值
            last_max_value = maxitr[j - 1]

            # 如果还可以装下
            if j >= weight:
                """
                这是为了j - weight >= 0, 不出现索引错误
                真正的判断是 maxitr[j - weight]: 得到的是刚好满足当前重量的背包容量的最大价值
                """
                maxitr[j] = max(last_max_value, maxitr[j - weight] + value)

        print(i, maxitr)












