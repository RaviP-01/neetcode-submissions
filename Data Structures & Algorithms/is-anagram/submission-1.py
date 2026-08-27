class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        n = len(s)
        m = len(t)
        b = False
        if n != m:
            return b
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1
        for i in range(len(t)):
            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1
        if d1 == d2:
            b = True
        return b
        