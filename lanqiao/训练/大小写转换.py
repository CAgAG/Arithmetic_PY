if __name__ == '__main__':
    s = input().strip()
    ss = ''
    for i in s:
        if i.isupper():
            ss += i.lower()
        else:
            ss += i.upper()
    print(ss)