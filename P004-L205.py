# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    # Runtime: O(n)
    def isIsomorphic(self, s: str, t: str) -> bool:
        sTranslator = {}
        tTranslator = {}
        slen = len(s)
        for i in range(slen):
            schar = s[i]
            tchar = t[i]
            if not schar in sTranslator and not tchar in tTranslator:
                sTranslator[schar] = tchar
                tTranslator[tchar] = schar
                continue
            if ((schar in sTranslator and sTranslator[schar] != tchar)
                or (tchar in tTranslator and tTranslator[tchar] != schar)):
                return False
        return True
    # end isIsomorphic
# end Solution
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.isIsomorphic("egg", "add") == True
    assert sol.isIsomorphic("foo", "bar") == False
    assert sol.isIsomorphic("paper", "title") == True
    print(sol.isIsomorphic("badc", "baba"))
