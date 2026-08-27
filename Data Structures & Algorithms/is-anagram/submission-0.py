class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b = True
        if len(s) != len(t):
            return False
        st = sorted(s)
        ss = sorted(t)
        b = (ss == st)
        
        return b
        