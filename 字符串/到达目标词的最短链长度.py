"""
    相邻单词间仅有一个字母不同
"""


# 判断两个字符串是否只有一个字符不同
def isAdjacent(a: str, b: str):
    i = 0
    count = 0
    while i < len(a):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            return False
        i += 1

    return True


def shortestChain(start: str, target: str, arr: list):
    q = []
    # 单词, 长度
    item = [start, 1]
    q.append(item)
    while len(q) > 0:
        cur, L = q[-1]
        # q.pop()
        for it in arr:
            if isAdjacent(cur, it):
                item = [it, L + 1]
                q.append(item)
                # 防止重复遍历
                arr.remove(it)
                if it == target:
                    return item[1], q

    return 0


if __name__ == '__main__':
    arr = [
        'pooN', 'pbcc', 'zamc', 'polc', 'pbca', 'pblc', 'polN',
    ]
    start = 'TooN'
    targrt = 'pbca'

    result = shortestChain(start, targrt, arr)
    print("长度: ", result[0])
    print('路径: ', result[1])
