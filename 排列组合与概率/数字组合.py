"""
    4 不能出现在第三个位置
    3, 5 不相邻
"""


class conb:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        # 是否已经访问过
        self.visited = [False] * self.n
        self.result = set()
        self.combination = ''
        self.graph = self.genGraph()

    # n: 列表长度
    # 构造图
    def genGraph(self):
        graph = [[-1] * self.n for _ in range(self.n)]
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                # 对角线
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = 1
                j += 1
            i += 1
        return graph

    # 深度搜索
    def depthSearch(self, start: int):
        self.visited[start] = True
        self.combination += str(self.arr[start])
        if len(self.combination) == self.n:
            # 第三个不能为 4
            if self.combination.find('4') != 2:
                self.result.add(self.combination)
        j = 0
        while j < self.n:
            if self.graph[start][j] == 1 and self.visited[j] == False:
                self.depthSearch(j)
            j += 1
        # 删去最后一个字符
        self.combination = self.combination[:-1]
        self.visited[start] = False

    def GetAllComb(self):
        # 确保 3, 5 不可达
        self.graph[3-1][5-1] = 0
        self.graph[5-1][3-1] = 0

        i = 0
        while i < self.n:
            self.depthSearch(i)
            i += 1

        return self.result


if __name__ == '__main__':
    c = conb([1, 2, 3, 4, 5])
    print(c.GetAllComb())
