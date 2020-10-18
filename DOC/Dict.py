"""
    从Python 3.6开始，默认的字典变成有序字典
    可以直接使用==进行等值判断

    合并字典，相同 key 的 value 相加:
        两个字典取并集，重点在于对相同key的value相加。

    python3,dict.keys() 类似set； | 并集  & 交集 - 差集
"""
from collections import Counter

if __name__ == '__main__':
    d1 = {
        '1': 1,
        '2': 2,
        '3': 3
    }
    d2 = {
        '2': 3,
        '3': 3,
        '1': 1
    }
    d3 = {
        '1': 1,
        '2': 2,
        '4': 3
    }
    d4 = {
        '1': 1,
        '3': 3,
        '2': 2,
        '4': 4
    }
    d5 = {
        '2': 2,
        '1': 1,
        '3': 3
    }

    print(d1 == d2)
    print(d1 == d3)
    print(d2 == d3)
    print(d1 == d4)
    print(d1 == d5)

    # 合并字典, key 相同则合并
    print(dict(Counter(d1) + Counter(d2)))  # 适用于value 大于0 的情况

    print(d4.keys() - d1.keys())

    A = {'a': 11, 'b': 22}
    B = {'c': 48, 'd': 13}
    # update() 把字典B的键/值对更新到A里, key不能相同否则会被覆盖
    A.update(B)
    print(A)
    # 与update 效果相同
    print({**A, **B})
