def RemovePare(Str: str):
    if Str is None:
        return

    if Str[0] != '(' or Str[-1] != ')':
        return None

    # ( 数量
    num = 0
    newStr = '('
    for s in Str[1: -1]:
        if s == '(':
            num += 1
        elif s == ')':
            num -= 1
        else:
            newStr += s
    if num != 0:
        return None
    newStr += ')'
    return newStr


if __name__ == '__main__':
    Str = '(1nnc( i(om(xa)))())'

    print(RemovePare(Str))
