import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort(reverse=True)



if __name__ == '__main__':
    sol = Solution()
    print(sol.maxHeight([[2,1]]))
