from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        nrow, ncol = len(matrix), len(matrix[0])
        self.partial_sum = [[0] * ncol for _ in range(nrow)]
        for r, vals in enumerate(matrix):
            for c, val in enumerate(vals):
                if c == 0:
                    self.partial_sum[r][c] = val
                else:
                    self.partial_sum[r][c] = val + self.partial_sum[r][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            res += self.partial_sum[r][col2]
            res -= ((self.partial_sum[r][col1 - 1] if col1 > 0 else 0)
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    pass