

from typing import List


class Solution:
    def magic_square(self, top_i, top_j, size, grid):
        target = sum(grid[top_i][top_j:top_j + size])
        
        # check rows
        for i in range(top_i, top_i + size):
            if sum(grid[i][top_j:top_j + size]) != target:
                return False
        
        # check columns
        for j in range(top_j, top_j + size):
            col_sum = 0
            for i in range(top_i, top_i + size):
                col_sum += grid[i][j]
            if col_sum != target:
                return False
        
        # check diagonals
        right_diag = sum(grid[top_i + d][top_j + d] for d in range(size))
        left_diag = sum(grid[top_i + d][top_j + size - 1 - d] for d in range(size))
        if right_diag != target or left_diag != target:
            return False
        
        return True
    
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if m == 1 or n == 1:
            return 1
        max_size = 1
        
        for size in range(2, min(m, n) + 1):
            for top_i in range(m - size + 1):
                for top_j in range(n - size + 1):
                    if self.magic_square(top_i, top_j, size, grid):
                        max_size = max(max_size, size)
        
        return max_size

grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]       
obj = Solution()
print(obj.largestMagicSquare(grid))