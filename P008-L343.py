# https://leetcode.com/problems/integer-break/
# Runtime: 24 ms -> beats 98.65% of users with Python3

class Solution:
    # Runtime: O(n^2)
    def integerBreak(self, n: int) -> int:
        memo = { 2: 1, 3: 2 }
        for m in range(4, n + 1):
            # calculate integerBreak(m)
            maxProd = 0
            for i in range(2, m - 1):
                maxProd = max(maxProd, i * memo[m - i], i * (m - i))
            memo[m] = maxProd
        return memo[n]
    # end integerBreak
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.integerBreak(2) == 1
    assert sol.integerBreak(10) == 36
    print(sol.integerBreak(5))
