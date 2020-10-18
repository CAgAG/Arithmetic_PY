
if __name__ == '__main__':
    n = int(input())
    m = int(input())

    graph = {}

    for _ in range(m):
        a, b = list(map(int, input().split()))
        l1 = graph.setdefault(a, set())
        l1.add(b)
        l2 = graph.setdefault(b, set())
        l2.add(a)

    ans = 0
    visited = set()
    for p1 in range(1, n + 1):
        same = set()
        same.add(p1)
        for p2 in range(p1 + 1, n):
            gp2 = graph[p2]
            if len(gp2 - same) == 0:
                pass

    print(ans)










