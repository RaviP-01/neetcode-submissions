class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0
        # Go through the list and increment the count if i is 1 else set it to 0.
        # Set res to max of res or count.
        for i in nums:
            count = count + 1 if i == 1 else 0
            res = max(res, count)
        return res
