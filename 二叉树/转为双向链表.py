from BiTree import BiTNode, Arr2Tree
from Array import RandArr


class DeLink:
    def __init__(self):
        self.pHead = None
        self.pEnd = None


link = DeLink()


def InOrderBSTree(root: BiTNode):
    if root is None:
        return

    # 转换root 的左子树
    InOrderBSTree(root.lchild)

    root.lchild = link.pEnd
    if link.pEnd is None:
        link.pHead = root
    else:
        link.pEnd.rchild = root

    link.pEnd = root
    InOrderBSTree(root.rchild)


if __name__ == '__main__':
    length = 10
    arr = RandArr(length)

    root = Arr2Tree(arr, 0, length - 1)

    InOrderBSTree(root)

    cur = link.pHead
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.rchild

    print()

    cur = link.pEnd
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.lchild
