from LinkNode import Node, ShowLink, List2Link


# None 无环, 否则返回slow和fast相遇的节点
def IsLoop(head: Node):
    if (head or head.next) is None:
        return None

    slow = head.next
    fast = head.next

    while (fast and fast.next) is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None

# 找到环的入口处
def FindLoopNode(head, meetNode: Node):
    first = head.next
    second = meetNode
    while first != second:
        first = first.next
        second = second.next

    return first


if __name__ == '__main__':
    head = List2Link([i for i in range(10)])
    ShowLink(head)

    # 构造 环
    p = head.next
    while p.next is not None:
        p = p.next

    print(p.data, "->", head.next.next.next.data)
    p.next = head.next.next.next

    meetNode = IsLoop(head)
    print('meetNode: ', meetNode.data if meetNode is not None else "None")
    if meetNode is not None:
        loopNode = FindLoopNode(head, meetNode)
        print('入口: ', loopNode.data)









