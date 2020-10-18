# 存权重
w = [0]
# 邻接表
g = {}


# 点作为根节点时的最大权和
def dfs(root, parent):
    for child in g[root]:
        if child != parent:
            dfs(child, root)
            if w[child] > 0:
                w[root] += w[child]


if __name__ == '__main__':
    n = int(input())
    w.extend(input().strip().split(' '))
    w = list(map(lambda x: int(x), w))

    for i in range(n - 1):
        line = input().strip().split(' ')
        g.setdefault(int(line[0]), []).append(int(line[1]))
        g.setdefault(int(line[1]), []).append(int(line[0]))

    dfs(1, 0)
    print(max(w))
    print(w)
