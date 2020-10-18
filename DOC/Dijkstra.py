import heapq
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def init_distance(graph, start):
    distance = {start: 0}
    for k in graph.keys():
        if k is not start:
            # 无穷大
            distance[k] = math.inf
    return distance


def dijkstra(graph, start):
    visited = set()
    pq = []
    # 优先队列
    heapq.heappush(pq, (0, start))
    distance = init_distance(graph, start)

    parent = {start: None}
    while pq:
        dis, u = heapq.heappop(pq)
        visited.add(u)
        for v in graph[u].keys():
            if v not in visited:
                if dis + graph[u][v] < distance[v]:
                    heapq.heappush(pq, (dis + graph[u][v], v))
                    distance[v] = dis + graph[u][v]
                    parent[v] = u

    return parent, distance


if __name__ == '__main__':
    parent, distance = dijkstra(graph, 'A')
    print(parent)
    print(distance)
