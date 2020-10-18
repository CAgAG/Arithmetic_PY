# words是否由其他元素组成
def isContain(arr: list, words: str):
    tp = words
    for s in arr:
        if s == words:
            continue

        if s in tp:
            tp = tp.replace(s, '')

    if tp == '':
        return words
    return None


def GetlongStr(arr: list):
    arr.sort(key=len, reverse=True)
    for s in arr:
        if isContain(arr, s) is not None:
            return s


if __name__ == '__main__':
    arr = [
        'test', 'asd', 'hjda', 'lksaod', 'hjdatestasd', 'nbcyBHA', 'nbcyBHAtestlksaod'
    ]

    print(GetlongStr(arr))
