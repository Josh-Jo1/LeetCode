# https://leetcode.com/problems/jump-game/
# Bottom-up approach runtime: 3236 ms -> beats 11.41% of users with Python3
# Top-down approach runtime: 5421 ms -> beats 5.89% of users with Python3
# Online approach runtime: 346 ms -> beats 79.71% of users with Python3

class Solution:
    # Bottom-up approach

    # # Runtime: O(n^2)
    # def canJump(self, nums: list[int]) -> bool:
    #     numsLen = len(nums)
    #     if numsLen < 2: return True
    #     memo = {}
    #     for i in range(numsLen - 2, -1, -1):
    #         # calculate canJump(i)
    #         memo[i] = False
    #         # jump directly?
    #         if i + nums[i] >= numsLen - 1:
    #             memo[i] = True
    #             continue
    #         # jump closer
    #         for j in range(i + 1, i + nums[i] + 1):
    #             if memo[j]:
    #                 memo[i] = True
    #                 break
    #     return memo[0]
    # # end canJump

    # Top-down approach

    # # Runtime: O(n^2)
    # def dp(self, idx: int) -> bool:
    #     if idx in self.memo: return self.memo[idx]
    #     self.memo[idx] = False
    #     # jump directly?
    #     if idx + self.nums[idx] >= self.numsLen - 1:
    #         self.memo[idx] = True
    #         return True
    #     # jump closer
    #     for i in range(1, self.nums[idx] + 1):
    #         reachedEnd = self.dp(idx + i)
    #         if reachedEnd:
    #             self.memo[idx] = True
    #             return True
    #     return False
    # # end dp

    # def canJump(self, nums: list[int]) -> bool:
    #     self.numsLen = len(nums)
    #     self.nums = nums
    #     if self.numsLen < 2: return True
    #     self.memo = {}
    #     return self.dp(0)
    # # end canJump

    # Online solution
    # Imagine a car driving the length of the array and refuelling only when the car's gas is less than what is currently available.
    # The car is the person jumping. They start a new jump (refuel) whenever the current jump distance is less than if they started a new jump.
    # https://leetcode.com/problems/jump-game/solutions/4534808/super-simple-intuitive-8-line-python-solution-beats-99-92-of-users/

    # Runtime: O(n)
    def canJump(self, nums: list[int]) -> bool:
        jumpDistAvailable = 0
        for n in nums:
            if jumpDistAvailable < 0:
                return False
            if n > jumpDistAvailable:
                jumpDistAvailable = n
            jumpDistAvailable -= 1
        return True
    # end canJump
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.canJump([2,3,1,1,4]) == True
    assert sol.canJump([3,2,1,0,4]) == False
