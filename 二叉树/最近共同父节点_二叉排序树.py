from BiTree import BiTNode, Arr2Tree
from StackT import StackArr, StackLink

StackType = StackArr


# 路径对比法
# 得到从root到node的路径
def GetPathFromRoot(root: BiTNode, node: BiTNode, stack: StackType):
    if root is None:
        return False
    if root == node:
        stack.push(root)
        return True
    """
        如果node 在root的左,右子树上
        那么root 就是node 的祖先, 加入栈
    """
    if GetPathFromRoot(root.lchild, node, stack) or \
            GetPathFromRoot(root.rchild, node, stack):
        stack.push(root)
        return True
    return False


def FindParentNode(root: BiTNode, node1: BiTNode, node2: BiTNode):
    stack1 = StackType()  # root -> node1
    stack2 = StackType()  # root -> node2

    GetPathFromRoot(root, node1, stack1)
    GetPathFromRoot(root, node2, stack2)

    commonParent = None
    while stack1.top() == stack2.top():
        commonParent = stack1.top()
        stack1.pop()
        stack2.pop()
    return commonParent


# 后序遍历法
def FindParentNodeByPost(root: BiTNode, node1: BiTNode, node2: BiTNode):
    if root is None or root == node1 or root == node2:
        return root

    left = FindParentNodeByPost(root.lchild, node1, node2)
    right = FindParentNodeByPost(root.rchild, node1, node2)

    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root


if __name__ == '__main__':
    arr = [
        i for i in range(1, 11)
    ]
    root = Arr2Tree(arr, 0, len(arr) - 1)
    node1 = root.lchild.lchild.lchild
    node2 = root.lchild.rchild

    res = FindParentNodeByPost(root, node1, node2)
    print(f'{node1.data}, {node2.data}')
    if res is not None:
        print(res.data)
