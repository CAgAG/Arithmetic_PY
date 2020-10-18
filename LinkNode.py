import random


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def RandHead(num: int):
    head = Node(-1)

    h = head
    i = 0
    while i < num:
        p = Node(random.randint(0, 100))

        h.next = p
        h = p

        i += 1
    return head


def List2Link(List: list):
    head = Node(-1)
    h = head
    for v in List:
        p = Node(v)

        h.next = p
        h = p
    return head


def ShowLink(head: Node):
    p = head.next
    while p is not None:
        print(p.data, end="->")
        p = p.next
    print("None")


if __name__ == '__main__':
    head = RandHead(10)
    head2 = List2Link([1, 1, 2])
    ShowLink(head)
    ShowLink(head2)
