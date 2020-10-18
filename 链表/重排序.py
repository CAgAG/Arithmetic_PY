from LinkNode import Node, RandHead, ShowLink


# input: l0->l1->l2->...->ln-1->ln
# out: l0->ln->l1->ln-1->...

# 找到中间节点
def FindMidNode(head: Node):
    if (head or head.next) is None:
        return head

    # 快慢指针
    fast = head
    slow = head
    slowPre = head

    while (fast and fast.next) is not None:
        slowPre = slow
        slow = slow.next
        fast = fast.next.next
    # 断开, 分为2个独立链表, head 和 slow
    slowPre.next = None
    return slow


# 对不带头节点的链表反转
def Reverse(head: Node):
    if (head or head.next) is None:
        return head

    pre = head
    cur = head.next
    pre.next = None

    while cur is not None:
        Next = cur.next
        cur.next = pre
        pre = cur
        cur = Next

    return pre


# 重排序
def Reoder(head: Node):
    if (head or head.next) is None:
        return

    # 前半部分
    cur1 = head.next
    mid = FindMidNode(head.next)
    # 后半部分
    cur2 = Reverse(mid)

    while cur1.next is not None:
        tp = cur1.next
        cur1.next = cur2
        cur1 = tp

        tp = cur2.next
        cur2.next = cur1
        cur2 = tp
    cur1.next = cur2


if __name__ == '__main__':
    head = RandHead(6)
    ShowLink(head)
    Reoder(head)
    ShowLink(head)
