from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        max_area = 0

        def mark_island(r: int, c: int) -> int:
            if (not 0 <= r < nrows) or (not 0 <= c < ncols) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                area += mark_island(i, j)
            return area
        
        for r in range(nrows):
            for c in range(ncols):
                max_area = max(max_area, mark_island(r, c))
        return max_area
            


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxAreaOfIsland([[1,0],[0,0]]))
    print(sol.maxAreaOfIsland([[1,0,1],[0,0,1]]))
