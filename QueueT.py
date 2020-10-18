import Array
from LinkNode import Node, ShowLink, List2Link, RandHead


class QueueArr:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0  # 默认一直为0

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def getFront(self):
        return self.front

    def getRear(self):
        return self.rear

    def getRearData(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def deQueue(self):
        if self.isEmpty():
            return

        self.queue.pop(0)
        self.front -= 1

    def enQueue(self, data):
        self.queue.append(data)
        self.rear += 1


class QueueLink:
    def __init__(self):
        self.head = Node(-1)
        self.end = self.head

    def isEmpty(self):
        return self.head.next is None

    def size(self):
        if self.isEmpty():
            return 0
        p = self.head.next
        size = 1  # + end
        while p != self.end:
            size += 1
            p = p.next
        return size

    def enQueue(self, data):
        data = Node(data)
        self.end.next = data
        self.end = data

    def deQueue(self):
        if self.isEmpty():
            return
        self.head.next = self.head.next.next


    def getFont(self):
        return self.head.next

    def getRear(self):
        return self.end

    def getFrontData(self):
        return self.head.next.data


if __name__ == '__main__':
    q = QueueArr()
    q2 = QueueLink()

    for i in Array.RandArr(10):
        q2.enQueue(i)

    print(q2.getFrontData())
    q2.deQueue()
    q2.deQueue()
    print(q2.getFrontData())
    print(q2.isEmpty())
