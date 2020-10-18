from LinkNode import Node, ShowLink, List2Link


def Reverse(head: Node):
    if (head or head.next) is None:
        return

    cur = head.next
    pre = head
    # Next = None
    # 待翻转指针 cur 和 cur.next
    while (cur and cur.next) is not None:
        Next = cur.next.next

        # pre->cur.next->cur->Next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = Next

        pre = cur
        cur = Next


if __name__ == '__main__':
    head = List2Link([
        i for i in range(10)
    ])
    ShowLink(head)
    Reverse(head)
    ShowLink(head)
