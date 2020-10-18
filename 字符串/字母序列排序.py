# 返回字符串按字母权重的值
def Compare(Str: str, alpha: list):
    result = 0
    for s in Str:
        if s in alpha:
            result += alpha.index(s)
    return result


def Sort(arr: list, alpha: list):
    return arr.sort(key=lambda x: Compare(x, alpha), reverse=True)


if __name__ == '__main__':
    alpha = list('dgecfboa')
    arr = [
        'bed', 'dog', 'dear', 'eye'
    ]

    for a in arr:
        print(Compare(a, alpha), end=" ")
    print()

    Sort(arr, alpha)
    print(arr)
