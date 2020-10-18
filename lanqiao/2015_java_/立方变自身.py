def f(x):
    result = 0
    for i in str(x):
        result += int(i)
    return result

if __name__ == '__main__':
    count = 0
    for i in range(1, 99):
        if i == f(i**3):
            count += 1
    print(count)