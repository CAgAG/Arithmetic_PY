"""
    数字——数据类型相关：bool，int，float，complex
    数字——进制转换相关：bin，oct，hex     转为: 二进制, 八进制, 十六进制
        转为10进制
        int('10')
        int('10',16)
        int('0x10',16)
        int('10',8)
        int('010',8)
        int('10',2)
    数字——数学运算：abs，divmod，min，max，sum，round，pow

    序列——列表和元组相关的：list和tuple
    序列——字符串相关的：str，ord，chr
                        函数ord()和chr()是一对功能相反的函数，
                        函数ord()用来返回单个字符的Unicode码，
                        而函数chr()则是用来返回Unicode编码对应的字符。
    reversed 保留原列表，返回一个反向的迭代器
    字典和集合：dict，set，frozenset   --- frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
    数据集合：len，sorted，enumerate，all，any，zip，filter，map, reduce

    在python里，{},[],()，等都等价于False！
"""
if __name__ == '__main__':
    # divmod: 返回除法和取余结果--int类型
    div, mod = divmod(10, 3)
    print(div, mod)

    # pow 幂运算
    # 2**5 % 3
    print(pow(2, 5, 3))

    # 绝对值最大小值
    # max(key=abs)
    # min(key=abs)

    # 区别字母大小写
    print('1'.islower())
    print('A'.isupper())

    """
        filter()函数接收一个函数 f 和一个list, 这个函数 f 的作用是对每个元素进行判断, 返回 True或
        False, filter()根据判断结果自动过滤掉不符合条件的元素, 返回由符合条件元素组成的新list
    """
    arr = [i for i in range(10)]
    # 只要偶数
    print(list(filter(lambda x: x % 2 == 0, arr)))

    """
        map(): 对每个元素进行操作
    """
    print(list(map(lambda x: x ** 2, arr)))
    # 相邻值相等
    arr1 = [1, 2, 2, 4, 6]
    print(all(map(lambda x, y: x == y, arr1[:-1], arr1[1:])))

    """
        reduce: 元素累积
    """
    from functools import reduce

    print(reduce(lambda x, y: x + y, arr))

    """
        zip: 对应位置打包, 多余的不要 
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9, 10]
    print(list(zip(a, b, c)))

    from itertools import product
