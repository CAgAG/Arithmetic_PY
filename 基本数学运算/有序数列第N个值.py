"""
    可被 2, 3, 5 整除
"""


def search(n: int):
    i = 1
    count = 0
    while True:
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            count += 1
        if count == n:
            break
        i += 1
    return i


if __name__ == '__main__':
    print(search(1500))
