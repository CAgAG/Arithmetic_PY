# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

from collections import Counter

if __name__ == '__main__':
    arr = [2, 3, 1, 0, 2, 5, 3]

    k, v = Counter(arr).most_common(1)[0]
    if v > 1:
        print(k)


