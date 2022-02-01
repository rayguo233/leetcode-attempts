import heapq
from functools import lru_cache
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        visited = {(0, 0)}  # type: set[Tuple[int, int]]
        hq = [(grid[0][0], 0, 0)]  # type: List[Tuple[int, int, int]]
        max_dep = grid[n-1][n-1]
        while hq:
            dep, row, col = heapq.heappop(hq)
            max_dep = max(max_dep, dep)
            for next_r, next_c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= next_r < n and 0 <= next_c < n and (next_r, next_c) not in visited:
                    if next_r == next_c == n-1:
                        return max_dep
                    visited.add((next_r, next_c))
                    heapq.heappush(hq, (grid[next_r][next_c], next_r, next_c))

        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.swimInWater([[0,2],[1,3]]))
