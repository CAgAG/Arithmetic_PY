def base62_encode(num, alphabet):
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

if __name__ == '__main__':
    n, XORnum = input().strip().split(' ')
    n = int(n)
    XORnum = int(XORnum)
    a = list(input().strip())

    output = []
    for _ in range(n):
        av = input().strip()
        number = int(av[2:])
        number ^= XORnum
        num = base62_encode(number, a)
        output.append('BV' + str(num))

    for out in output:
        print(out)
