"""
    每个磁盘大小d[i]
    每个分区大小p[i]
"""


def is_allocable(d: list, q: list):
    # 磁盘分区下标
    index = 0
    # 磁盘数量
    length = len(d)

    for space in q:  # 分区大小
        # 找到符合条件的磁盘
        while index < length and space > d[index]:
            index += 1

        if index >= length:
            return False

        # 给分区分配磁盘
        d[index] -= space
    return True


if __name__ == '__main__':
    d = [120, 120, 256]
    p = [60, 60, 80, 90, 100]

    print(is_allocable(d, p))
