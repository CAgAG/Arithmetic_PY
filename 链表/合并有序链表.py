from LinkNode import Node, ShowLink, List2Link

def Merge(h1, h2: Node):
    if (h1 or h1.next) is None:
        return h2
    if (h2 or h2.next) is None:
        return h1

    cur1 = h1.next
    cur2 = h2.next

    # 升序
    if cur1.data > cur2.data:
        head = h2
        cur = cur2
        cur2 = cur2.next
    else:
        head = h1
        cur = cur1
        cur1 = cur1.next

    while (cur1 and cur2) is not None:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next

    if cur1 is not None:
        cur.next = cur1
    if cur2 is not None:
        cur.next = cur2
    return head

if __name__ == '__main__':
    h1 = List2Link([
        i for i in range(20, 30, 2)
    ])
    h2 = List2Link([
        i for i in range(20, 30, 3)
    ])
    ShowLink(Merge(h1, h2))



















