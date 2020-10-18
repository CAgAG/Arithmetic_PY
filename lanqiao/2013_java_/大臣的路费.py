class node:
    def __init__(self, num, dis):
        self.num = num
        self.distance = dis

def money(dis):
    return 11 * dis + dis * (dis - 1) / 2

def dfs(From, num, dis):
    global Max_distance, pnt

    isLeaf = True

    neighbors = g[num]
    for neighbor in neighbors:
        if neighbor.num == From:
            continue
        isLeaf = False
        dfs(num, neighbor.num, dis + neighbor.dis)
    # 是叶子节点
    if isLeaf and dis > Max_distance:
        Max_distance = dis
        pnt = num

# 邻接矩阵
g = {}
Max_distance = -1
pnt = None

if __name__ == '__main__':
    m = int(input())
    for _ in range(m):
        a, b, c = input().strip().split(' ')
        a, b, c = int(a), int(b), int(c)
        g.get(a, []).append(node(b, c))
        g.get(b, []).append(node(a, c))

    dfs(1, 1, 0)
    dfs(pnt, pnt, 0)
    print(Max_distance)
    print(money(Max_distance))

