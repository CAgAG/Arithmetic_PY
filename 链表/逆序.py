from LinkNode import Node
from LinkNode import RandHead, ShowLink


# 就地排序
def Reverse(head: Node):
    if head == None or head.next == None:
        return

    cur = head.next
    Next = cur.next  # 记入当前的下一个节点
    cur.next = None  # 断开

    # 去头节点
    pre = cur
    cur = Next
    # pre->cur(Next)

    while cur.next != None:
        Next = cur.next
        # pre 和 cur 节点互换
        cur.next = pre
        pre = cur
        # cur = cur.next # 注意错误
        cur = Next
    cur.next = pre
    head.next = cur


# 插入法
def Reverse2(head: Node):
    if head is None or head.next is None:
        return

    cur = head.next.next
    head.next.next = None
    while cur is not None:
        Next = cur.next
        cur.next = head.next
        head.next = cur
        cur = Next


# 递归
# 适用于不带头节点的单链表
def Reverse3(head: Node):
    if head == None or head.next == None:
        return head
    else:
        # 反转后面的节点
        newHead = Reverse3(head.next)

        head.next.next = head
        head.next = None
        return newHead


# 不推荐
def Reverse4(head: Node):
    if head is None:
        return
    firstNode = head.next
    newHead = Reverse3(firstNode)
    head.next = newHead
    return newHead


# 不推荐
# 适用于不带头节点的单链表
def Reverse5(firstNode: Node):
    if firstNode is None:
        return
    Reverse5(firstNode.next)
    print(firstNode.data, end='->')


if __name__ == '__main__':
    head = RandHead(10)
    ShowLink(head)
    Reverse4(head)
    ShowLink(head)
