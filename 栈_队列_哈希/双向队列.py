"""
    模拟排号系统
"""
from collections import deque


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.seq = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getSeq(self):
        return self.seq

    def setSeq(self, seq):
        self.seq = seq

    def equals(self, user):
        return self.id == user.id

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, seq: {self.seq}'


class SQueue:
    def __init__(self):
        self.q = deque()

    def enQueue(self, user: User):
        user.setSeq(len(self.q) + 1)
        self.q.append(user)

    def deQueue(self):
        self.q.popleft()
        self.updateSeq()

    def deQueue4User(self, user: User):
        self.q.remove(user)
        self.updateSeq()

    def updateSeq(self):
        i = 1
        for user in self.q:
            user.setSeq(i)
            i += 1

    def __str__(self):
        info = ''
        for user in self.q:
            info += user.__str__() + '\n'
        return info


if __name__ == '__main__':
    Squeue = SQueue()

    Squeue.enQueue(User(1, "u1"))
    Squeue.enQueue(User(2, 'u2'))
    out = User(3, "u3")
    Squeue.enQueue(out)
    Squeue.enQueue(User(4, 'u4'))

    Squeue.deQueue()
    Squeue.deQueue4User(out)

    print(Squeue)













