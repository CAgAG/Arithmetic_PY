# 检测（x,y）这个位置是否合法（不会被其他皇后攻击到）
def is_attack(queue, x, y):
    for i in range(x):
        if queue[i] == y or abs(x - i) == abs(queue[i] - y):
            return True
    return False

# 按列来摆放皇后
def put_position(n, queue, col):
    for i in range(n):
        if not is_attack(queue, col, i):
            queue[col] = i
            if col == n - 1:    # 此时最后一个皇后摆放好了，打印结果。
                print(queue)
            else:
                put_position(n, queue, col + 1)


n = 4       # 这里是n 就是n皇后
queue = [None for i in range(n)]        # 存储皇后位置的一维数组，数组下标表示皇后所在的列，下标对应的值为皇后所在的行。
put_position(n, queue, 0)
