from LinkNode import Node, RandHead, ShowLink


def IsIntersect(h1, h2: Node):
    if (h1 or h1.next) is None:
        return None
    if (h2 or h2.next) is None:
        return None

    cur1, cur2 = h1.next, h2.next
    n1, n2 = 0, 0  # 记录链表长度

    while cur1.next is not None:
        cur1 = cur1.next
        n1 += 1
    while cur2.next is not None:
        cur2 = cur2.next
        n2 += 1

    # 尾节点是否相等
    if cur1 == cur2:
        # 同一起跑线
        if n1 > n2:
            while n1 - n2 > 0:
                h1 = h1.next
                n1 -= 1
        if n1 < n2:
            while n2 - n1 > 0:
                h2 = h2.next
                n2 -= 1

        # 2个链表同时前进, 找到相同节点
        while h1 != h2:
            h1 = h1.next
            h2 = h2.next
        return h1
    else:
        return None


if __name__ == '__main__':
    h1 = RandHead(2)
    h2 = RandHead(2)
    tp = RandHead(2)

    h1.next.next.next = tp.next
    h2.next.next.next = tp.next

    ShowLink(h1)
    ShowLink(h2)

    result = IsIntersect(h1, h2)
    print(result.data if result is not None else "None")