import itertools

if __name__ == '__main__':
    # 排列(不放回的拿出)
    # 不出现(a, a),  n 只能小于等于sequence的长度
    # 排列元素个数
    # 相当于 itertools.combinations_with_replacement()
    print(list(itertools.permutations('abc', 2)))
    # 不允许元素重复出现的组合(不放回), 即有(a, b), 不出现(b, a)
    print(list(itertools.combinations('abc', 2)))
    """
        itertools.product(sequence，repeat) 　::: 允许重复元素出现
         从sequence中拿出repeat个数做排列（repeat关键字传参）
         有放回的拿出  repeat与sequence的长度无关。
    """
    # 均出现
    print(list(itertools.product('abc', repeat=2)))

    """
    去除相邻重复值
    from itertools import groupby

    input:[k for k, g in groupby('AAAABBBCCDAABBB')] 
    output:['A', 'B', 'C', 'D', 'A', 'B']
    
    input:[list(g) for k, g in groupby('AAAABBBCCD')]
    output：[['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
    """