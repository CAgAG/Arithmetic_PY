"""
input:
降序    -------> 升序
^       x1 -> x2 -> x3 -> ...
|       |     |
|       x11   x21       |
|       x12
out:
    x1 -> x11 -> x12 -> x2 -> x21 -> x3
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


def InsrtRights(node: Node, data: list):
    p = node
    for i in data:
        tp = Node(i)
        p.right = tp
        p = p.right


def InsertDown(node: Node, data: list):
    p = node
    for i in data:
        tp = Node(i)
        p.down = tp
        p = p.down

def Print(head: Node):
    p = head
    while p is not None:
        print(p.data, end='->')
        p = p.down
    print('None')


class MergeList:
    def __init__(self):
        pass

    # 合并a, b 链表
    def Merge(self, a, b: Node):
        if a is None:
            return b
        if b is None:
            return a

        if a.data < b.data:
            result = a
            result.down = self.Merge(a.down, b)
        else:
            result = b
            result.down = self.Merge(a, b.down)

        return result

    def Flatten(self, root: Node):
        if root is None or root.right is None:
            return root
        # 处理root.right
        root.right = self.Flatten(root.right)
        # 合并
        root = self.Merge(root, root.right)
        return root


if __name__ == '__main__':
    LinkList = Node(3)

    InsrtRights(LinkList, [
        4, 5, 6
    ])
    InsertDown(LinkList, [
        4, 5, 6
    ])
    InsertDown(LinkList.right, [
        7, 8
    ])

    mergeList = MergeList()
    head = mergeList.Flatten(LinkList)
    Print(head)







