import itertools

"""
B组第9题

标题：带分数

    100 可以表示为带分数的形式：100 = 3 + 69258 / 714

    还可以表示为：100 = 82 + 3546 / 197

    注意特征：带分数中，数字1~9分别出现且只出现一次（不包含0）。

    类似这样的带分数，100 有 11 种表示法。

题目要求：
从标准输入读入一个正整数N (N<1000*1000)
程序输出该数字用数码1~9不重复不遗漏地组成带分数表示的全部种数。
注意：不要求输出每个表示，只统计有多少表示法！


例如：
用户输入：
100
程序输出：
11

再例如：
用户输入：
105
程序输出：
6


资源约定：
峰值内存消耗（含虚拟机） < 64M
CPU消耗  < 3000ms


请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。

所有代码放在同一个源文件中，调试通过后，拷贝提交该源码。
注意：不要使用package语句。不要使用jdk1.6及以上版本的特性。
注意：主类的名字必须是：Main，否则按无效代码处理。
"""


def f(a, b, c):
    return a + b / c


def build(num):
    count = 0
    for comb in itertools.permutations('123456789', 9):
        all = ''.join(comb)
        for i in range(1, 9):
            a = int(all[:i])
            if a > num:
                break
            for j in range(8, i, -1):
                b = int(all[i: j])
                c = int(all[j:])
                if c > b:
                    break
                if f(a, b, c) == num:
                    count += 1
    return count


if __name__ == '__main__':
    print(build(105))
