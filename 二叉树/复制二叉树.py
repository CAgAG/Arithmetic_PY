from BiTree import BiTNode, Arr2Tree, InOrder
from Array import RandArr


def CopyTree(root: BiTNode):
    if root is None:
        return None

    node = BiTNode()
    node.data = root.data

    node.lchild = CopyTree(root.lchild)
    node.rchild = CopyTree(root.rchild)
    return node


if __name__ == '__main__':
    arr = RandArr(10)

    root = Arr2Tree(arr, 0, len(arr) -1)
    root2 = CopyTree(root)

    InOrder(root)
    print()
    InOrder(root2)