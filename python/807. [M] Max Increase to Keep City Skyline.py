from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [0] * len(grid)
        col_max = [0] * len(grid[0])
        for r, row in enumerate(grid):
            for c, h in enumerate(row):
                row_max[r] = max(h, row_max[r])
                col_max[c] = max(h, col_max[c])
        
        res = 0
        for r, row in enumerate(grid):
            for c, h in enumerate(row):
                inc = min(row_max[r], col_max[c]) - h
                res += inc
        
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxIncreaseKeepingSkyline([[3,3,4],
                                         [0,4,0]]))
