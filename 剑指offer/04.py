# https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

def Bin_Search(target, arr: list):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid_index = (left + right) // 2
        mid = arr[mid_index]
        if mid > target:
            right = mid_index - 1
        elif mid < target:
            left = mid_index + 1
        else:
            return True

    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7, 9],
              [2, 4, 6, 8, 10],
              [11, 13, 15, 17, 19],
              [12, 14, 16, 18, 20],
              [21, 22, 23, 24, 25]]

    target = 13
    m, n = len(matrix), len(matrix[0])

    index = 0
    flag = False
    while index < m and index < n:
        flag = Bin_Search(target, matrix[index][index:])
        if flag:
            print('true')
            break
        flag = Bin_Search(target, [matrix[i][index] for i in range(index, m)])
        if flag:
            print('true')
            break
        index += 1
    if not flag:
        print('false')
