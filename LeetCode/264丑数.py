# https://leetcode-cn.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        rec = [0] * n
        rec[0] = 1
        for i in range(1, n):
            ugly = min(rec[p2] * 2, rec[p3] * 3, rec[p5] * 5)
            rec[i] = ugly

            if ugly == rec[p2]*2:
                p2 += 1
            if ugly == rec[p3]*3:
                p3 += 1
            if ugly == rec[p5]*5:
                p5 += 1

        return rec[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(n=10))