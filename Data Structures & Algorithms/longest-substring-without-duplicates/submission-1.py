class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ld = {}
        l,r = 0, 0
        length = 0
        while r <= len(s)-1:
            if s[r] in ld:
                l = max(ld[s[r]] + 1, l)
            ld[s[r]] = r
            length = max(length, r-l+1)
            r += 1
        return length

