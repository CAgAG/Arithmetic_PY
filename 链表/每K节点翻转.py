from LinkNode import Node, ShowLink, List2Link

# 对不带头节点的链表进行翻转
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


def ReverseK(head: Node, k: int):
    if (head or head.next) is None:
        return

    i = 1
    pre = head
    begin = head.next

    while begin is not None:
        end = begin
        # 前进k步
        while i < k:
            if end.next is not None:
                end = end.next
            else:
                break
            i += 1
        # 下一个区间头节点
        Next = end.next
        end.next = None # 断开
        pre.next = Reverse(begin)

        begin.next = Next
        pre = begin
        begin = Next

        i = 1


if __name__ == '__main__':
    head = List2Link([
        i for i in range(10)
    ])
    ShowLink(head)
    ReverseK(head, 3)
    ShowLink(head)










