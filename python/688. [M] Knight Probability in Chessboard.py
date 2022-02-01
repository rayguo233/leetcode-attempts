from functools import lru_cache
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    @lru_cache(None)
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 0 <= row < n and 0 <= column < n
        if not (0 <= row < n and 0 <= column < n):
            return 0
        next_moves = [(row-2, column+1), (row-2, column-1), (row-1, column+2), (row-1, column-2),
                      (row+2, column+1), (row+2, column-1), (row+1, column+2), (row+1, column-2)]
        sum_pos = 0
        for r, c in next_moves:
            sum_pos += self.knightProbability(n, k-1, r, c)
        return sum_pos / 8

if __name__ == '__main__':
    sol = Solution()
    print(sol.knightProbability(n = 3, k = 2, row = 0, column = 0))
