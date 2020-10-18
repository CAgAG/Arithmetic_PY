import copy

class QFind:
    """
        2: 白
        3: 黑
    """
    def __init__(self, n: int, Map: list):
        self.n = n
        self.Map = Map
        self.count = 0

    def isOk(self, i, j, num):
        # print(i, j)
        if self.Map[i][j] != 1:
            return False
        # 行
        for index, p in enumerate(Map[i]):
            if p == num and index != j:
                return False
        # 列, 对角线
        for p in range(self.n):
            if Map[p][j] == num and p != i:
                return False
            if Map[p][p] == num and p != i:
                return False

        return True

    def DFS(self):
        pass

    def getResult(self):
        self.DFS()
        return self.count


if __name__ == '__main__':
    Map = []
    n = int(input())
    for i in range(n):
        tp = input().strip().split(' ')
        tp = [int(i) for i in tp]
        Map.append(tp)

    Q = QFind(n, Map)
    print(Q.getResult())
