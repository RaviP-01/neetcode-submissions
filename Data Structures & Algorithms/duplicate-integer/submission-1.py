class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = False
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
                b = True
                break
            else:
                d[i] = 1
        return b