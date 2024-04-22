# https://leetcode.com/problems/restore-ip-addresses/
# Runtime: 34 ms -> beats 85.18% of users with Python3
#     - I did not use recursion in hopes of improving performance

class Solution:
    def isValidNumber(self, n: str, len: int) -> bool:
        return len == 1 or (n[0] != "0" and int(n) < 256)
    # end isValidNumber

    # Runtime: O(1)
    def restoreIpAddresses(self, s: str) -> list[str]:
        sLen = len(s)
        if sLen not in range(4, 17): return []
        retval = []
        for w in range(1, 4):
            part1 = s[0:w]
            if not self.isValidNumber(part1, w): break
            if sLen - w > 9: continue
            endRange1 = min(4, sLen - w + 1)
            for x in range(1, endRange1):
                part2 = s[w:w+x]
                if not self.isValidNumber(part2, x): break
                if sLen - w - x > 6: continue
                endRange2 = min(4, sLen - w - x + 1)
                for y in range(1, endRange2):
                    part3 = s[w+x:w+x+y]
                    if not self.isValidNumber(part3, y): break
                    if sLen - w - x - y > 3: continue
                    endRange3 = min(4, sLen - w - x - y + 1)
                    for z in range(1, endRange3):
                        part4 = s[w+x+y:w+x+y+z]
                        if not self.isValidNumber(part4, z): break
                        if sLen - w - x - y - z > 0: continue
                        retval.append(f"{part1}.{part2}.{part3}.{part4}")
        return retval
    # end restoreIpAddresses
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.restoreIpAddresses("25525511135") == ["255.255.11.135","255.255.111.35"]
    assert sol.restoreIpAddresses("0000") == ["0.0.0.0"]
    assert sol.restoreIpAddresses("101023") == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
