class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        ptr = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums[i] = nums[ptr]
                ptr -= 1
            else:
                count += 1
        return count