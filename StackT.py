import Array
from LinkNode import Node, ShowLink


class StackArr:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def top(self):
        if not self.isEmpty():
            return self.stack[self.size() - 1]
        else:
            return None

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def push(self, data):
        self.stack.append(data)

    def Show(self):
        print(self.stack)


class StackLink:
    def __init__(self):
        self.head = Node(-1)

    def isEmpty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.head.next
        while p is not None:
            p = p.next
            size += 1
        return size

    def push(self, data):
        data = Node(data)
        data.next = self.head.next
        self.head.next = data

    def pop(self):
        if not self.isEmpty():
            data = self.head.next.data
            self.head.next = self.head.next.next
            return data
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self.head.next.data
        else:
            return None

    def Show(self):
        ShowLink(self.head)


if __name__ == '__main__':
    s = StackArr()
    s2 = StackLink()

    for i in Array.RandArr(10):
        # s.push(i)
        s2.push(i)

    print(s2.pop())
    print(s2.pop())
    print(s2.size())
    print(s2.isEmpty())
    print(s2.top())
