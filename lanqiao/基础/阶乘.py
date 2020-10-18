def f(num):
    if num == 1:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


if __name__ == '__main__':
    n = int(input())
    print(f(n))
