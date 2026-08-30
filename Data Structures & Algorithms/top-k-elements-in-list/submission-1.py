class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n log n) - runtime
        # O(n) - space
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        return list(sorted(d, key=d.get, reverse=True)[:k])