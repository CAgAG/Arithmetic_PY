from BiTree import BiTNode, Arr2Tree, InOrder
from Array import RandArr

def FindMaxPath(root: BiTNode, maxs: int):
    if root is None:
        return 0

    left = FindMaxPath(root.lchild, maxs)
    right = FindMaxPath(root.rchild, maxs)

    sums = left + right + root.data

    leftMax = root.data + left
    rightMax = root.data + right

    tpMax = max(leftMax, rightMax, sums)

    if tpMax > maxs:
        maxs = tpMax

    subMax = left if left > right else right
    return root.data + subMax


if __name__ == '__main__':
    root = BiTNode()
    root.data = 2
    left = BiTNode()
    left.data = 3
    right = BiTNode()
    right.data = 5
    root.lchild = left
    root.rchild = right

    maxs = FindMaxPath(root, -2**31)
    print(maxs)

