from LinkNode import Node, RandHead, ShowLink


def FindLastK(head: Node, k: int):
    if (head or head.next) is None:
        return head

    # 快慢指针
    slow = head.next
    fast = head.next
    i = 0

    # 前进k步
    while i < k and fast is not None:
        fast = fast.next
        i += 1

    if i < k:
        return None

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow

# 变形
# 链表右旋k个位置
def RotateK(head: Node, k: int):
    if (head or head.next) is None:
        return

    # 快慢指针
    slow = head.next
    fast = head.next
    i = 0

    # 前进k步
    while i < k and fast is not None:
        fast = fast.next
        i += 1

    if i < k:
        return

    # slow 指向倒数第k+1个元素
    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    slowPre = slow
    slow = slow.next # 倒数第k个节点
    slowPre.next = None
    fast.next = head.next
    head.next = slow



if __name__ == '__main__':
    head = RandHead(6)
    ShowLink(head)
    KNode = FindLastK(head, 3)
    print(KNode.data if KNode is not None else "None")
    RotateK(head, 3)
    ShowLink(head)
