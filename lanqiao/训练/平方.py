def charge(x):
    r1 = pow(x, 1/2)
    charge = r1 - int(r1)
    return charge == 0

if __name__ == '__main__':
    num = int(input())
    if num < 0:
        print(0)
    else:
        for i in range(num, num*2):
            if charge(i):
                print(i)
                break