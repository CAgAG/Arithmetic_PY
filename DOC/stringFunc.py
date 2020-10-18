import string

if __name__ == '__main__':
    print(string.digits)  # 输出包含数字0~9的字符串
    print(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串
    print(string.ascii_lowercase)  # 包含所有小写字母的字符串
    print(string.ascii_uppercase)  # 包含所有大写字母的字符串

    print([chr(i) for i in range(65, 91)])  # 所有大写字母
    print([chr(i) for i in range(97, 123)])  # 所有小写字母
    print([chr(i) for i in range(48, 58)])  # 所有数字