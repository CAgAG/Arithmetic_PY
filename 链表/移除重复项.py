from LinkNode import Node, ShowLink, List2Link


def RemoveDup(head: Node):
    if head is None or head.next is None:
        return

    outerCur = head.next  # 用于外层循环
    # innerCur = None # 内层循环, 遍历outerCur后面的节点
    # innerPre = None # innerCur 的前驱节点

    while outerCur is not None:
        innerCur = outerCur.next
        innerPre = outerCur
        while innerCur is not None:
            # 找到重复节点
            if outerCur.data == innerCur.data:
                innerPre.next = innerCur.next
            else:
                innerPre = innerCur
            innerCur = innerCur.next

        outerCur = outerCur.next


# 递归
def RemoveDup2Recursion(head: Node):
    if head.next is None:
        return head

    # p = None
    cur = head
    # 对以head.next 为首的子链表删除重复项
    head.next = RemoveDup2Recursion(head.next)
    p = head.next
    # 找出以head.next 为首的子链表中与head 节点相同的节点, 并删除
    while p is not None:
        if head.data == p.data:
            cur.next = p.next
            p = cur.next
        else:
            p = p.next
            cur = cur.next

    return head


def RemoveDup2(head: Node):
    if head is None:
        return
    head.next = RemoveDup2Recursion(head.next)


# 辅助空间
def RemoveDup3(head: Node):
    if (head or head.next) is None :
        return head

    Map = dict()
    pre = head
    cur = head.next

    while cur is not None:
        if Map.get(cur.data) is not None:
            pre.next = cur.next
        else:
            pre = cur
            Map[cur.data] = 1
        cur = cur.next
    return head


if __name__ == '__main__':
    head = List2Link([
        1, 2, 1, 7, 8, 9, 3, 4, 3, 2, 1
    ])
    ShowLink(head)
    RemoveDup3(head)
    ShowLink(head)
