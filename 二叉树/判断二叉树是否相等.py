from BiTree import BiTNode, Arr2Tree
from Array import RandArr


def IsEqual(root1, root2: BiTNode):
    if (root1 and root2) is None:
        return True

    if root1 is None and root2 is not None:
        return False

    if root1 is not None and root2 is None:
        return False

    if root1.data == root2.data:
        return IsEqual(root1.lchild, root2.lchild) and \
               IsEqual(root1.rchild, root2.rchild)
    else:
        return False


if __name__ == '__main__':
    length = 10
    arr = RandArr(length)

    root1 = Arr2Tree(arr, 0, length - 1)
    root2 = Arr2Tree(arr, 0, length - 1)
    root3 = Arr2Tree(RandArr(length), 0, length - 1)

    print(IsEqual(root1, root2))
    print(IsEqual(root1, root3))
