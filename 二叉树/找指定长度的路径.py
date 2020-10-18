from BiTree import BiTNode, Arr2Tree, InOrder
from Array import RandArr

def FindRoad(root: BiTNode, num: int, sums: int, v: list):
    sums += root.data
    v.append(root.data) # 存路径

    # 找到叶子节点, 且==num
    if (root.lchild and root.rchild) is None and sums == num:
        i = 0
        while i < len(v):
            print(v[i], end=" ")
            i += 1
        print()

    if root.lchild is not None:
        FindRoad(root.lchild, num, sums, v)
    if root.rchild is not None:
        FindRoad(root.rchild, num, sums, v)

    # 清除遍历的路径
    sums -= v[-1]
    v.remove(v[-1])


if __name__ == '__main__':
    arr = [
        i for i in range(1, 11)
    ]
    root = Arr2Tree(arr, 0, len(arr)-1)

    s = []
    FindRoad(root, 12, 0, s)
    print(s)






