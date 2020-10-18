from collections import deque


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def Arr2Tree(arr: list, start, end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = (start + end + 1) // 2
        root.data = arr[mid]
        root.lchild = Arr2Tree(arr, start, mid - 1)
        root.rchild = Arr2Tree(arr, mid + 1, end)
    return root


def InOrder(root: BiTNode):
    if root is None:
        return

    if root.lchild is not None:
        InOrder(root.lchild)
    print(root.data, end=" ")
    if root.rchild is not None:
        InOrder(root.rchild)


def PreOrder(root: BiTNode):
    if root is None:
        return

    print(root.data, end=" ")
    if root.lchild is not None:
        InOrder(root.lchild)
    if root.rchild is not None:
        InOrder(root.rchild)


def PostOrder(root: BiTNode):
    if root is None:
        return

    if root.lchild is not None:
        InOrder(root.lchild)
    if root.rchild is not None:
        InOrder(root.rchild)
    print(root.data, end=" ")


def LevelOrder(root: BiTNode):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        print(p.data, end=" ")
        if p.lchild is not None:
            queue.append(p.lchild)
        if p.rchild is not None:
            queue.append(p.rchild)


if __name__ == '__main__':
    arr = [i for i in range(10)]

    root = Arr2Tree(arr, 0, len(arr) - 1)
    # InOrder(root)
    # print()
    PreOrder(root)
    print()
    # PostOrder(root)
    # print()
    LevelOrder(root)
