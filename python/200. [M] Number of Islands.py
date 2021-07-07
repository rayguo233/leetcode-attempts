# https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid grid which represents a map
# of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume
# all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        def mark(row, col):
            if 0 <= row < num_rows and 0 <= col < num_cols and grid[row][col] == '1':
                grid[row][col] = '0'
                return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            return []

        res = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1':
                    res += 1
                    stack = [(r, c)]
                    while stack:
                        row, col = stack.pop(0)
                        stack += mark(row, col)

        return res


if __name__ == '__main__':
    sol = Solution()
    assert(sol.rob([0]) == 0)
    assert(sol.rob([2,1,4]) == 6)
    assert(sol.rob([2,4]) == 4)
    assert(sol.rob([2,1,4,8]) == 10)
    assert(sol.rob([2,1,4,8,9]) == 15)
