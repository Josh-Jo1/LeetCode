# https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution:
    # Runtime: O(n)
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        value = 0
        for hour in hours:
            if hour >= target:
                value += 1
        return value
    # end numberOfEmployeesWhoMetTarget
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2) == 3
    assert sol.numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6) == 0
