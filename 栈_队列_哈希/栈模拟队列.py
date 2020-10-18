from StackT import StackArr, StackLink
import Array

StackType = StackArr


class StackQueue:
    def __init__(self):
        self.A = StackType()
        self.B = StackType()

    def push(self, data):
        self.A.push(data)

    def pop(self):
        if self.B.isEmpty():
            while not self.A.isEmpty():
                self.B.push(self.A.top())
                self.A.pop()

        top = self.B.top()
        self.B.pop()
        return top


if __name__ == '__main__':
    queue = StackQueue()

    for i in Array.RandArr(10):
        queue.push(i)

    print(queue.pop())
    print(queue.pop())
