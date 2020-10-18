if __name__ == '__main__':
    for i in range(32):
        b = bin(i)[2:]
        length = len(b)
        if length != 5:
            b = '0'*(5-length)+b
        print(b)