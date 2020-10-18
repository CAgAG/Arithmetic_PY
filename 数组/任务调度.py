"""
    最短时间完成任务
    a, b 机器: 7min, 10min
    6个任务
"""


def chargeMission(M: list, N: int):
    if M is None or N <= 0:
        return None

    # 服务器数量
    length = len(M)
    # 计算每个服务器的分配任务时间
    proTime = [0] * length

    for _ in range(N):
        # 第一台服务器时间设为耗时最短
        minTime = proTime[0] + M[0]
        minIndex = 0

        # 其他服务器
        # 选出耗时短的服务器
        j = 1
        while j < length:
            if minTime > proTime[j] + M[j]:
                minTime = proTime[j] + M[j]
                minIndex = j

            j += 1
        # 耗时最少的服务器, 时间累计
        proTime[minIndex] += M[minIndex]
    return proTime


if __name__ == '__main__':
    M = [7, 10]
    N = 6
    charge = chargeMission(M, N)
    print(charge)
    print(max(charge))
