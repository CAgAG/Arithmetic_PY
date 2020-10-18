# 判断字符是否为中文
def isChs(c: str):
    return True if c >= '\u4e00' and c <= '\u9fff' else False


def truncate(s: str, L: int):
    if s == None or s == '' or L <= 0:
        return ''

    sub = ''
    # 记录长度
    count = 0
    for c in s:
        if count < L:
            if isChs(c):
                # 超过
                if count + 3 > L:
                    return sub

                count += 3
                sub += c
            else:
                count += 1
                sub += c
        else:
            break

    return sub


if __name__ == '__main__':
    s = '人AVBN的GHJK'

    print(truncate(s, 7))
