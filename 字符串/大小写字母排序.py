def Reverse(chars: list):
    length = len(chars)
    begin = 0
    end = length - 1

    # 类似快排
    while begin < end:
        # 正向找下一个大写字母
        while chars[begin].islower() and end > begin:
            begin += 1
        # 反向找下一个小写字母
        while chars[end].isupper() and end > begin:
            end -= 1

        chars[begin], chars[end] = chars[end], chars[begin]


if __name__ == '__main__':
    chars = 'snBXHBasdLo'
    # 字符串是不可变对象，不要试图用下标的方法去改变字符串的值
    chars = list(chars)
    Reverse(chars)

    print(''.join(chars))
