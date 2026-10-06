class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for n in range(len(matrix)):
            l, r = 0, len(matrix[n])-1
            while l <= r:
                m = l + (r - l) // 2
                if target > matrix[n][m]:
                    l = m + 1
                elif target < matrix[n][m]:
                    r = m - 1
                else:
                    return True

        return False