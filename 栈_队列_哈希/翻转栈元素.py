from StackT import StackArr, StackLink
import Array

StackType = StackArr


# 把栈底元素移到栈顶
def MoveBottom2Top(s: StackType):
    if s.isEmpty():
        return

    top = s.top()
    s.pop()
    if not s.isEmpty():
        # top 变化
        MoveBottom2Top(s)
        top2 = s.top()
        s.pop()

        s.push(top)
        s.push(top2)
    else:
        # 压入栈底元素
        s.push(top)


# 翻转
def Reverse(s: StackType):
    if s.isEmpty():
        return
    MoveBottom2Top(s)
    top = s.top()
    s.pop()
    # 从栈底向栈顶拿元素
    Reverse(s)
    s.push(top)


# 变形
# 排序
# 功能类似与冒泡的一趟排序
# 选出最小值到栈顶
def BubbleStep(s: StackType):
    if s.isEmpty():
        return
    top = s.top()
    s.pop()

    if not s.isEmpty():
        BubbleStep(s)
        top2 = s.top()
        # 对比相邻值大小
        if top > top2:
            s.pop()
            s.push(top)
            s.push(top2)
            return
    s.push(top)


# 与Reverse 相似
def SortStack(s: StackType):
    if s.isEmpty():
        return
    BubbleStep(s)
    top = s.top()
    s.pop()

    SortStack(s)
    s.push(top)


if __name__ == '__main__':
    s = StackType()

    for i in range(10):
        s.push(i)

    s.Show()
    print(s.top())
    BubbleStep(s)
    s.Show()
    BubbleStep(s)
    s.Show()
