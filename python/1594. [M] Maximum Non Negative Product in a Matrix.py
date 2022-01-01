from typing import List, Optional, Tuple

MAX, MIN = 0, 1

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        prev_row = [[1, 1]] * ncols
        for row, array in enumerate(grid):
            curr_row = [None] * ncols  # type: List[Optional[List[int, int]]]
            for col, val in enumerate(array):
                products = []
                if col == row == 0:
                    products += [val]
                if row > 0:
                    products += [val * prev_row[col][MAX], val * prev_row[col][MIN]]
                if col > 0:
                    products += [val * curr_row[col-1][MAX], val * curr_row[col-1][MIN]]
                curr_row[col] = [max(products), min(products)]
            # print(prev_row)
            prev_row, curr_row = curr_row, [None] * ncols
        # print(prev_row)
        res = max(prev_row[ncols-1] + [-1])
        if res == -1:
            return res
        return  res % (10 ** 9 + 7)

if __name__ == '__main__':
    pass
    sol = Solution()
    print(sol.maxProductPath([
        [-1,-2,-3],
        [-2,-3,-3],
        [-3,-3,-2]]))
