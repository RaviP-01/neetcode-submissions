class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        """ Check if the number is in dict, if it is return true else add to
            dict. """
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False