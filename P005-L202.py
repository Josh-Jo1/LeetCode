# https://leetcode.com/problems/happy-number/
# Runtime: 28 ms -> beats 95.22% of users with Python3

class Solution:
    def numToDigits(self, n) -> list[int]:
        num = n
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        digits.reverse()
        return digits
    # end numToDigits

    def isHappy(self, n: int) -> bool:
        num = n
        memo = []
        while True:
            if num == 1:
                return True
            if num in memo:
                return False
            memo.append(num)
            digits = self.numToDigits(num)
            num = sum([x**2 for x in digits])
    # end isHappy
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.isHappy(19) == True
    assert sol.isHappy(2) == False
