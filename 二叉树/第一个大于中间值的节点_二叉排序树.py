from BiTree import BiTNode, Arr2Tree, InOrder
from Array import RandArr


# 找最小值
def GetMin(root: BiTNode):
    if root is None:
        return root

    while root.lchild is not None:
        root = root.lchild

    return root


# 找最大值
def GetMax(root: BiTNode):
    if root is None:
        return root

    while root.rchild is not None:
        root = root.rchild

    return root


def GetNode(root: BiTNode):
    maxNode = GetMax(root)
    minNode = GetMin(root)

    # 找到中间值
    mid = (maxNode.data + minNode.data) / 2

    result = None
    while root is not None:
        if root.data <= mid:
            root = root.rchild
        else:
            result = root
            root = root.lchild

    return result


if __name__ == '__main__':
    root = Arr2Tree(RandArr(10), 0, 9)

    Node = GetNode(root)
    print(Node.data)
