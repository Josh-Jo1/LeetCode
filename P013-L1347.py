# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# First approach runtime: 164 ms -> beats 43.14% of users with Python3
# Second approach runtime: 174 ms -> beats 34.09% of users with Python3

class Solution:
    # First approach

    # # Runtime: O(n)
    # def minSteps(self, s: str, t: str) -> int:
    #     count = {}
    #     # Process s
    #     for char in s:
    #         if char in count:
    #             count[char] += 1
    #         else:
    #             count[char] = 1
    #     # Process t
    #     for char in t:
    #         if char in count:
    #             count[char] -= 1
    #         else:
    #             count[char] = -1
    #     # Determine result
    #     totalIncorrect = 0
    #     for key in count:
    #         totalIncorrect += abs(count[key])
    #     return totalIncorrect // 2
    # # end minSteps

    # Second approach (attempt at improved performance)

    # Runtime: O(n)
    def minSteps(self, s: str, t: str) -> int:
        length = len(s)     # same as t
        count = [0] * 26
        for i in range(0, length):
            # Process s
            count[ord(s[i]) - ord('a')] += 1
            # Process t
            count[ord(t[i]) - ord('a')] -= 1
        # Determine result
        totalIncorrect = 0
        for i in range(0, 26):
            totalIncorrect += max(count[i], 0)
        return totalIncorrect
    # end minSteps
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.minSteps("bab", "aba") == 1
    assert sol.minSteps("leetcode", "practice") == 5
    assert sol.minSteps("anagram", "mangaar") == 0
