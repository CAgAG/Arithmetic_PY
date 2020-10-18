# 打印1 ~ n
def prints(n: int):
    if n > 0:
        prints(n - 1)
        print(n, end=" ")


if __name__ == '__main__':
    prints(100)
