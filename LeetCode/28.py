def strStr(haystack: str, needle: str):
    try:
        i = haystack.index(needle)
        return i
    except Exception:
        return -1


def strStr2(haystack: str, needle: str):
    if needle == '':
        return 0
    start_index = 0
    length = len(needle)
    if length > len(haystack):
        return -1

    for _ in range(len(haystack)):
        if haystack[start_index] != needle[0]:
            start_index += 1
            continue
        n_index = 1
        flag = True
        for index in range(start_index + 1, start_index + length):
            if haystack[index] != needle[n_index]:
                flag = False
                break
            n_index += 1

        if flag:
            return start_index
    return -1


if __name__ == '__main__':
    print(strStr2('a', 'a'))
