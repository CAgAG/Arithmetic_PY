"""
    向集合中添加一个元素 s.add()
    随机删除s.pop()    指定删除s.remove() 与s.discard()   删除不存在的remove会报错 discard不会报错
    集合的交集& ,s.intersection()
    集合的并集 | ,s. union()
    集合的差集  s1.difference(s2) 将集合s1里去掉和s2交集的部分
    集合的交叉补集  s.symmetric_difference() 并集里去掉交集的部分
"""

if __name__ == '__main__':
    Set1 = set([i for i in range(10)])
    Set2 = set([i for i in range(7, 15)])

    # 交集
    print(Set1.intersection(Set2))
    print(Set1 & Set2)

    # 并集
    print(Set1.union(Set2))
    print(Set1 | Set2)

    # 差集
    print(Set1.difference(Set2))
    print(Set1 - Set2)

    # 交叉补集: 并集里去掉交集的部分
    print(Set1.symmetric_difference(Set2))




