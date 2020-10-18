# https://leetcode-cn.com/problems/ugly-number/solution/kuai-su-pan-duan-chou-shu-by-erik_chen/

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while True:
            last = num
            if num % 2 == 0:
                num //= 2 # or num >>= 1
            if num % 3 == 0:
                num //= 3
            if num % 5 == 0:
                num //= 5
            if num == 1:
                return True
            if last == num: # 除不了了
                return False