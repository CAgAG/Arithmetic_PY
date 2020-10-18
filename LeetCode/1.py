# https://leetcode-cn.com/problems/two-sum/

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6

    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            print([i, j])

