import random


# n个房子
def getRoom(n: int):
    room = [-1] * n
    i = 0
    while i < n:
        room[i] = random.randint(1, n)  # 1 ~ n 个金币
        i += 1
    print(room)
    return room


def search(room: list):
    # 找出前4个房间的最多金币数量
    max4 = 0
    for r in room[:4]:
        if r > max4:
            max4 = r

    for coin in room[4:]:
        if coin > max4:
            return True
    return False


if __name__ == '__main__':
    print(search(getRoom(10)))
