from LinkNode import Node, RandHead, ShowLink


# p: 给定删除的节点
def RemoveNode(p: Node):
    if (p or p.next) is None:
        return False
    p.data = p.next.data
    p.next = p.next.next
    return True

if __name__ == '__main__':
    head = RandHead(10)
    ShowLink(head)
    p = head.next.next
    if RemoveNode(p):
        ShowLink(head)
    else:
        ShowLink(head)