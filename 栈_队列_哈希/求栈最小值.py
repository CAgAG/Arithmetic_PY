from StackT import StackArr, StackLink
from Array import RandArr

StackType = StackArr


class MinStack():
    def __init__(self):
        self.stack = StackType()
        self.minStack = StackType()  # 栈顶永远存储stack最小值

    def push(self, data):
        self.stack.push(data)
        if self.minStack.isEmpty():
            self.minStack.push(data)
        else:
            if data < self.minStack.top():
                self.minStack.push(data)

    def pop(self):
        top = self.stack.top()
        self.stack.pop()
        if top == self.min():
            self.minStack.pop()
        return top

    def min(self):
        if self.minStack.isEmpty():
            return None
        else:
            return self.minStack.top()


if __name__ == '__main__':
    stack = MinStack()
    stack.push(1)
    print(stack.min())
    stack.push(2)
    print(stack.min())
    stack.push(-1)
    print(stack.min())
