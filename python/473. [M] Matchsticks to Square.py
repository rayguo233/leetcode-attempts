from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sm = sum(matchsticks)
        if sm % 4:
            return False
        side = sm // 4
        memo = {}

        def dfs() -> bool:



if __name__ == '__main__':
    sol = Solution()
    print(sol.makesquare([0,1]))
