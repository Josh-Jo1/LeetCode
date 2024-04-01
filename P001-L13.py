# https://leetcode.com/problems/roman-to-integer/

class Solution:
    converter = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # # Runtime: O(n)
    # def romanToInt(self, s: str) -> int:
    #     slen = len(s)
    #     if slen == 1:
    #         return self.converter[s]
    #     value = 0
    #     i = 1
    #     while i < slen:
    #         last = s[i - 1]
    #         curr = s[i]
    #         if self.converter[last] < self.converter[curr]:
    #             value += self.converter[curr] - self.converter[last]
    #             i += 2
    #             if i == slen:
    #                 value += self.converter[s[i - 1]]
    #         else:
    #             value += self.converter[last]
    #             i += 1
    #             if i == slen:
    #                 value += self.converter[curr]

    #     return value
    # # end romanToInt

    # Improved solution
    # Runtime: O(n)
    def romanToInt(self, s: str) -> int:
        slen = len(s)
        value = 0
        for i in range(slen):
            if i + 1 < slen and self.converter[s[i]] < self.converter[s[i + 1]]:
                value -= self.converter[s[i]]
            else:
                value += self.converter[s[i]]
        return value
    # end romanToInt
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("LVIII") == 58
    assert sol.romanToInt("MCMXCIV") == 1994
    print(sol.romanToInt("MDCXCV"))
