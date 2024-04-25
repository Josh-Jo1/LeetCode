# https://leetcode.com/problems/push-dominoes/
# Runtime: 161 ms -> beats 80.31% of users with Python3

class Solution:
    # Runtime: O(n)
    def pushDominoes(self, dominoes: str) -> str:
        dominoesLen = len(dominoes)
        # Determine all dominoes falling left
        leftDominoes = list(dominoes)
        time = 1
        for i in range(dominoesLen - 1, 0, -1):
            if (leftDominoes[i] == 'L' or leftDominoes[i].isdigit()) and leftDominoes[i - 1] == '.':
                leftDominoes[i - 1] = str(time)
                time += 1
            else:
                time = 1
        # Determine and compare to all dominoes falling right
        retval = list(dominoes)
        time = 0
        for i in range(0, dominoesLen):
            if leftDominoes[i].isdigit():
                if time == 0:
                    retval[i] = 'L'
                elif time < int(leftDominoes[i]):
                    retval[i] = 'R'
                    time += 1
                elif time == int(leftDominoes[i]):
                    retval[i] = '.'
                else:
                    retval[i] = 'L'
            elif leftDominoes[i] == 'R':
                time = 1
            elif leftDominoes[i] == '.' and time != 0:
                retval[i] = 'R'
            else:
                time = 0
        return ''.join(retval)
    # end pushDominoes
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.pushDominoes("RR.L") == "RR.L"
    assert sol.pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
    print(sol.pushDominoes(".L.R."))
