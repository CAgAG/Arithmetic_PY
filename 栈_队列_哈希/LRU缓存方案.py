from collections import deque


class LRU:
    def __init__(self, cacheSize: int):
        self.cacheSize = cacheSize
        self.queue = deque()
        self.hashSet = set()

    def isFull(self):
        return len(self.queue) == self.cacheSize

    def enQueue(self, data):
        if self.isFull():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()

        self.queue.appendleft(data)
        self.hashSet.add(data)

    def accessQueue(self, data):
        if data not in self.hashSet:
            self.enQueue(data)
        elif data != self.queue[0]:
            self.queue.remove(data)
            self.queue.appendleft(data)

    def __str__(self):
        return str(self.queue)


if __name__ == '__main__':
    lru = LRU(2)

    for i in [1, 3, 5, 1, 6]:
        lru.accessQueue(i)

    print(lru)




