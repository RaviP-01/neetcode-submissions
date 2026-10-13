class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for i in piles:
                total += math.ceil(float(i) / mid)
            if total <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k 