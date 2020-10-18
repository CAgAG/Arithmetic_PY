"""
    广度优先遍历
"""


def bfs(graph, start):
    visited = set()
    q = []
    q.append(start)  # 把起始点放入队列
    while q:
        u = q.pop(0)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
        print(u, end=" ")


def bfs_path(graph, start):
    visited = set()
    q = []
    q.append(start)  # 把起始点放入队列
    parent = {start: None}
    while q:
        u = q.pop(0)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
                parent[v] = u
        print(u, end=" ")

    print()
    # for k, v in parent.items():
    #     print(k, v)

    end = 3
    while end is not None:
        print(end, end='<-')
        end = parent[end]


if __name__ == '__main__':
    graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
    bfs(graph, start=1)
