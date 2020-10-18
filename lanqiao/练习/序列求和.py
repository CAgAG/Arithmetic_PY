def f(length):
    return length + length * (length - 1) // 2


if __name__ == '__main__':
   n = int(input())
   print(f(n))