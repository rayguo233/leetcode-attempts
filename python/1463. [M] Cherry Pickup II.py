import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter

UNREACHABLE = -1

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        dp = [[UNREACHABLE] * ncol for _ in range(ncol)]
        dp[0][ncol-1] = grid[0][0] + grid[0][ncol-1]
        for row in grid[1:]:
            curr_dp = [[UNREACHABLE] * ncol for _ in range(ncol)]
            for curr_c1 in range(ncol):
                for curr_c2 in range(curr_c1, ncol):
                    for prev_c1 in (curr_c1-1, curr_c1, curr_c1+1):
                        for prev_c2 in (curr_c2-1, curr_c2, curr_c2+1):
                            if curr_c1 <= curr_c2 and 0 <= prev_c1 < ncol and prev_c2 < ncol and dp[prev_c1][prev_c2] != UNREACHABLE:
                                if curr_c1 == curr_c2:
                                    cherry = row[curr_c1]
                                else:
                                    cherry = row[curr_c1] + row[curr_c2]
                                curr_dp[curr_c1][curr_c2] = max(dp[prev_c1][prev_c2] + cherry, curr_dp[curr_c1][curr_c2])
            dp = curr_dp
            # print(dp)
        return max(max(row) for row in dp)



if __name__ == '__main__':
    sol = Solution()
    print(sol.cherryPickup([[1, 2],
                            [5, 7]]))
    print(sol.cherryPickup([[3,1,1],
                            [2,5,1],
                            [1,5,5],
                            [2,1,1]]))
    print(sol.cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))
