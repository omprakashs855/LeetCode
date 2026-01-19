# Maximum Side Length of a Square with Sum Less than or Equal to Threshold


from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])

        if m == 1 or n == 1:
            for row_list in mat:
                if threshold in row_list:
                    return 1
            else:
                return 0
        
        if threshold < 2:
            for row_list in mat:
                if threshold in row_list:
                    return threshold
            else:
                return 0

        top_i, top_j = 0,0
        bot_i, bot_j = 1,1
        i, j = 0,0
        out = 0
        gap = 2

        # Solution not done yet



        return out


        
mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 4
obj = Solution()
print(obj.maxSideLength(mat, threshold))