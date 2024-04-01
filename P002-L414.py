# https://leetcode.com/problems/third-maximum-number/

class Solution:
    # Runtime: O(n)
    def thirdMax(self, nums: list[int]) -> int:
        firstMax = None
        secondMax = None
        thirdMax = None
        for i in nums:
            if i == firstMax or i == secondMax:
                continue
            if firstMax is None:
                firstMax = i
            elif i > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = i
            elif secondMax is None:
                secondMax = i
            elif i > secondMax:
                thirdMax = secondMax
                secondMax = i
            elif thirdMax is None:
                thirdMax = i
            elif i > thirdMax:
                thirdMax = i
        return thirdMax if thirdMax is not None else firstMax
    # end thirdMax
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.thirdMax([3,2,1]) == 1
    assert sol.thirdMax([1,2]) == 2
    assert sol.thirdMax([2,2,3,1]) == 1
    print(sol.thirdMax([1,2,2]))
