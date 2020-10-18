from BiTree import BiTNode, Arr2Tree, InOrder
from Array import RandArr


def ReverseTree(root: BiTNode):
    if root is None:
        return

    ReverseTree(root.lchild)
    ReverseTree(root.rchild)

    tp = root.lchild
    root.lchild = root.rchild
    root.rchild = tp


if __name__ == '__main__':
    root = Arr2Tree(RandArr(10), 0, 9)

    InOrder(root)

    ReverseTree(root)

    print()
    InOrder(root)