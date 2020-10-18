"""
    DFS: 深度优先遍历
"""


def dfs(graph, start):
    visited = set()
    q = []
    q.append(start)  # 把起始点放入队列
    while q:
        u = q.pop()
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
        print(u, end=" ")


if __name__ == '__main__':
    graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
    dfs(graph, 1)
