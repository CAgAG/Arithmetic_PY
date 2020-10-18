from LinkNode import Node, ShowLink, List2Link


#    个->十->百
# h1: 3->1->5
# h2: 1->2->3
# result:
#       513+321=834
#       4->3->8


def Add(h1, h2: Node):
    if (h1 or h1.next) is None:
        return h2
    if (h2 or h2.next) is None:
        return h2

    c = 0  # 记录进位
    p1 = h1.next
    p2 = h2.next
    # tp = None
    resultHead = Node(-1)
    p = resultHead

    while (p1 and p2) is not None:
        sums = p1.data + p2.data + c
        tp = Node(sums % 10)
        c = sums // 10
        p.next = tp
        p = tp

        p1 = p1.next
        p2 = p2.next

    # p2 长度 >= p1
    if p1 is None:
        while p2 is not None:
            sums = p2.data + c
            tp = Node(sums % 10)
            c = sums // 10
            p.next = tp
            p = tp

            p2 = p2.next
    # p1 长度 >= p2
    if p2 is None:
        while p1 is not None:
            sums = p1.data + c
            tp = Node(sums % 10)
            c = sums // 10
            p.next = tp
            p = tp

            p2 = p1.next

    # 如果还有进位
    if c == 1:
        tp = Node(1)
        p.next = tp

    return resultHead


if __name__ == '__main__':
    # 321
    h1 = List2Link([
        1, 2, 3
    ])
    # 9789
    h2 = List2Link([
        9, 8, 7, 9
    ])
    result = Add(h1, h2)
    ShowLink(result)
