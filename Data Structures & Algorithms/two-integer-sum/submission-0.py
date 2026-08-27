class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []
        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] in d:
                res.append(d.get(nums[i]))
                res.append(i)
                break
            else:
                d[comp] = i
        return res