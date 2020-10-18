import itertools


def getCard():
    return itertools.permutations('AA223344', 8)


def rule():
    index_map = dict()
    result = set()
    for comb in getCard():
        index_map.clear()
        flag = True
        for index, c in enumerate(comb):
            if index_map.get(c) is None:
                index_map[c] = index
            else:
                dis = index - index_map[c]
                if c == 'A' and (dis == 2):
                    index_map[c] = index
                elif c == '2' and (dis == 3):
                    index_map[c] = index
                elif c == '3' and (dis == 4):
                    index_map[c] = index
                elif c == '4' and (dis == 5):
                    index_map[c] = index
                else:
                    flag = False
                    break
        if flag:
            result.add(''.join(comb))
    return result


if __name__ == '__main__':
    print(rule())
