from BiTree import BiTNode, Arr2Tree
from Array import RandArr

maxSum = -2 ** 32
maxRoot = BiTNode()


def FindMaxSubTree(root):
    if root is None:
        return 0

    # 左子树和
    leftSum = FindMaxSubTree(root.lchild)
    # 右子树和
    rightSum = FindMaxSubTree(root.rchild)

    sums = leftSum + rightSum + root.data

    global maxSum, maxRoot
    if sums > maxSum:
        maxSum = sums
        maxRoot.data = root.data
    return sums


if __name__ == '__main__':
    length = 10
    arr = RandArr(length)

    root = Arr2Tree(arr, 0, length - 1)

    FindMaxSubTree(root)
    print(f'最大子树和: {maxSum}, true sum: {sum(arr)}')
    print(f'对应子树根: {maxRoot.data}')
