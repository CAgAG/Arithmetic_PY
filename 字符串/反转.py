def Reverse(Str: str):
    return Str[::-1]


# 变化
# 单词反转
def ReverseI(Words: str):
    Words = Words.split(' ')
    for i, s in enumerate(Words):
        Words[i] = Reverse(s)
    return ' '.join(Words)


if __name__ == '__main__':
    Str = '123456 90'
    print(ReverseI(Str))
