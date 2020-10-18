count = 0


def f(k, cnt):
    """
    :param k: 拿到几种牌
    :param cnt: 拿到几张牌
    :return:
    """
    if k > 13 or cnt > 13:
        return
    if cnt == 13:
        global count
        count += 1
        return

    for i in range(5):
        f(k + 1, cnt + i)


if __name__ == '__main__':
    f(0, 0)
    print(count)
