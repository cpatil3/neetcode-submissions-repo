class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = dict()
        countT = dict()

        for c in s:
            countS[c] = 1 + countS.get(c, 0)
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        for k in countS:
            if k not in countT:
                return False
            elif countS[k] != countT[k]:
                return False

        return True
