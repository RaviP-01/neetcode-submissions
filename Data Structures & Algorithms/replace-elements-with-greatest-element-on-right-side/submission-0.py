class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        pt1 = 0
        pt2 =  pt1
        res = [0] * len(arr)
        while (pt1 < len(arr)):
            if pt2 + 1 >= len(arr):
                pt1 += 1
                pt2 = pt1
                continue
            current = arr[pt2+1]
            if res[pt1] < current:
                res[pt1] = current
            pt2 += 1
            
        res[len(arr)-1] = -1
        return res