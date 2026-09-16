class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        count = 1
        max_count = 1
        if not nums:
            return 0
        list_nums = list(set_nums)
        list_nums.sort()
        for n in range(len(list_nums)):
            if n+1 < len(list_nums):
                if list_nums[n+1] == list_nums[n] + 1:
                    count += 1
                else:
                    count = 1
            max_count = max(max_count, count)
            
        return max_count