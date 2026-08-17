class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntT = {}
        cntS = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            cntT[t[i]] = 1 + cntT.get(t[i], 0)
            cntS[s[i]] = 1 + cntS.get(s[i], 0)
        return cntT == cntS