def checkDay(x):
    x = int(x)
    if x >= 0 and x <= 31:
        return True
    return False


def checkWeek(x):
    x = int(x)
    if x >= 1 and x <= 12:
        return True
    return False


def checkYear(num):
    if int('19' + num) >= 1960:
        return True, '19'
    if int('20' + num) <= 2059:
        return True, '20'
    return False, None


if __name__ == '__main__':
    arr = input().strip().split('/')
    flag, ret = checkYear(arr[0])
    if flag:
        if checkWeek(arr[1]) and checkDay(arr[2]):
            print('{}-{}-{}'.format(ret + arr[0], arr[1], arr[2]))
    flag, ret = checkYear(arr[-1])
    if flag:
        if checkWeek(arr[0]) and checkDay(arr[1]):
            print('{}-{}-{}'.format(ret + arr[-1], arr[0], arr[1]))
        if checkWeek(arr[1]) and checkDay(arr[0]):
            print('{}-{}-{}'.format(ret + arr[-1], arr[1], arr[0]))
