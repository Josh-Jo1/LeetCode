# https://leetcode.com/problems/multiply-strings/
# Runtime: 104 ms -> beats 20.69% of users with Python3
#     - I submitted `return str(int(num1) * int(num2))` and got 30ms,
#       which is where most of the submissions are, but this is cheating

class Solution:
    # Runtime: O(n*m)
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        num1Len = len(num1)
        num2Len = len(num2)
        retval = [0] * (num1Len + num2Len)
        for i in range(num1Len - 1, -1, -1):
            for j in range(num2Len - 1, -1, -1):
                retval[i + j + 1] += int(num1[i]) * int(num2[j])
                retval[i + j] += retval[i + j + 1] // 10
                retval[i + j + 1] %= 10
        idx = 0
        while retval[idx] == 0: idx += 1
        strval = ""
        while idx < num1Len + num2Len:
            strval += str(retval[idx])
            idx += 1
        return strval
    # end multiply
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.multiply("2", "3") == "6"
    assert sol.multiply("123", "456") == "56088"
