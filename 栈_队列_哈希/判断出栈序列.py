"""
    根据入栈序列判断可能的出栈序列
"""
from StackT import StackArr, StackLink

StackType = StackLink


def isPopSerial(push, pop: str):
    if (push or pop) is None:
        return False

    pushLen = len(push)
    popLen = len(pop)
    if pushLen != popLen:
        return False

    pushIndex, popIndex = 0, 0
    stack = StackType()
    while pushIndex < pushLen:
        stack.push(push[pushIndex])
        pushIndex += 1
        while (not stack.isEmpty()) and stack.top() == pop[popIndex]:
            stack.pop()
            popIndex += 1

    return stack.isEmpty() and popIndex == pushIndex


if __name__ == '__main__':
    push = '123456'
    pop = '123465'
    print(isPopSerial(push, pop))
