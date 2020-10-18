"""
    找到满足 a+b = c+d 的数对
"""


# 存储数对
class pair:
    def __init__(self, first, second: int):
        self.first = first
        self.second = second


def FindPair(arr: list):
    # key= 数对的和, value= 数对
    sumPair = dict()
    length = len(arr)

    i = 0
    while i < length:
        j = i + 1
        while j < length:
            sums = arr[i] + arr[j]
            if sums not in sumPair:
                sumPair[sums] = pair(i, j)
            else:
                p = sumPair[sums]
                print(f'({arr[p.first]}, {arr[p.second]})', f'({arr[i]}, {arr[j]})')
            j += 1
        i += 1


if __name__ == '__main__':
    arr = [3, 4, 7, 8, 9, 10, 20, 11, 19]
    FindPair(arr)
