def IsPostOrder(arr: list, start, end: int):
    if arr is None:
        return False

    # 最后一个元素必定是根节点
    root = arr[end]
    # 找到第一个大于root的值, 那么前面所有节点都位于root左子树上
    i = start
    while i < end:
        if arr[i] > root:
            break
        i += 1

    # 反推
    j = i
    while j < end:
        if arr[j] < root:
            return False
        j += 1

    left = True
    right = True
    # 判断小于root的值, 是否满足
    if i < start:
        left = IsPostOrder(arr, start, i - 1)
    # 判断大于root的值, 是否满足
    if j < end:
        right = IsPostOrder(arr, i, end)

    return left and right


if __name__ == '__main__':
    """
                    4
                2       6
            1     3   5     7
    """
    arr = [
        1, 3, 2, 5, 7, 6, 4
    ]
    result = IsPostOrder(arr, 0, len(arr) - 1)

    print(result)
