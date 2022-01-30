import heapq
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, deque


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrows, ncols = len(heights), len(heights[0])
        hq = [(0, (0, 0))]
        visited = {}
        while True:
            # print(hq)
            (max_efft, (r, c)) = heapq.heappop(hq)
            if r == nrows - 1 and c == ncols - 1:
                return max_efft
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= next_r < nrows and 0 <= next_c < ncols:
                    # print(heights[next_r][next_c], heights[r][c])
                    next_max_efft = max(max_efft, abs(heights[next_r][next_c] - heights[r][c]))
                    if (next_r, next_c) not in visited or visited[(next_r, next_c)] > next_max_efft:
                        heapq.heappush(hq, (next_max_efft, (next_r, next_c)))
                    visited[(next_r, next_c)] = min(next_max_efft, visited.get((next_r, next_c), float('inf')))



if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumEffortPath([[1,2,3],
                                 [3,8,4],
                                 [5,3,5]]), 1)
    print(sol.minimumEffortPath([[1,2,2],
                                 [3,8,2],
                                 [5,3,5]]), 2)
    print(sol.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
