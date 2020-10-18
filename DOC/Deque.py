""""
    api: 类似于list
    双向队列: 从右边添加和从左边弹出
"""
from collections import deque

import random

if __name__ == '__main__':
    count = 10
    i = 0

    q = deque()
    while i < count:
            q.append(random.randint(-10, 10))
            print(q)
            i += 1

    # 与列表相同, 移除右边
    # while len(q) != 0:
    #     q.pop()
    #     print(q)

    # 移除左边
    while len(q) != 0:
        q.popleft()
        print(q)

    """
    append + popleft = 队列
    append + pop = 栈 
    """

    """
    count：数量
    entend：参数是一个可迭代变量，在右端按照迭代顺序添加
    extendleft：同上，不过是在左端按照迭代顺序添加
    index： 和list的相类似
    insert: 和list的相同，插入元素insert(index,obj),
            在index前插入元素，如果index超过长度就会插到最后,
            如果长度已经是最长，再插入会报错
    remove：同list：用于移除列表中某个值的第一个匹配项。
    rotate：循环移动，为正: 全体右移，为负: 全体左移
    """
