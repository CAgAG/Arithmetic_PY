# s2 是否是s1 子串
def isRotate(s1: str, s2: str):
    if (s1 or s2) is None:
        return False

    s1 *= 2

    if s1.find(s2) != -1:
        return True
    return False

if __name__ == '__main__':
    s1 = 'waterbottle'
    s2 = 'erbottlewat'

    print(isRotate(s1, s2))