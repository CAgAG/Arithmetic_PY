"""
    求2个路径的相对路径
"""


def GetRelativePath(path1: str, path2: str):
    if (path1 or path2) is None:
        return

    relativePath = ''

    # 不同路径起始长度
    diff1 = diff2 = 0

    i = 0
    j = 0
    len1 = len(path1)
    len2 = len(path2)

    while i < len1 and j < len2:
        # 目录相同, 继续遍历
        if path1[i] == path2[j]:
            if path1[i] == '/':
                diff1 = i
                diff2 = j
            i += 1
            j += 1
        else:
            # 不同目录
            # path1 非公共部分转为 '../'
            diff1 += 1
            while diff1 < len1:
                if path1[diff1] == '/':
                    relativePath += '../'
                diff1 += 1

            diff2 += 1
            relativePath += path2[diff2:]
            return relativePath


if __name__ == '__main__':
    p1 = 'a/b/c/op/pp/txt.c'
    p2 = 'a/b/c/tt/word.c'

    print(GetRelativePath(p1, p2))
