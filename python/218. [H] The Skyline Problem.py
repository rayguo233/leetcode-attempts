import collections
from heapq import heappop, heappush
import itertools
from lib2to3.pytree import WildcardPattern
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter

HQ_X, HQ_Y = 1, 0
RES_X, RES_Y = 0, 1


class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = [[-1, 0]]
        buildings.sort()
        hq = []
        for x0, x1, y in itertools.chain(
                buildings,
            [[float('inf'), float('inf'),
              float('inf')]]):
            most_recent_x = -1
            while hq and hq[0][HQ_X] < x0:
                # print('***', hq, res, x0, x1, y)
                prev_y, prev_x = heappop(hq)
                prev_y = -prev_y
                if prev_x <= res[-1][RES_Y]:
                    continue
                most_recent_x = max(prev_x, most_recent_x)
                if prev_y != res[-1][RES_Y]:
                    res.append([prev_x, prev_y])

            if not hq:
                res.append([most_recent_x, 0])

            if not hq or y > -hq[0][HQ_Y]:
                res.append([x0, y])

            heappush(hq, (-y, x1))

        return res[2:-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.getSkyline([[1, 3, 2], [2, 4, 3]]))
    print(sol.getSkyline([[1, 3, 2], [2, 4, 3], [5, 6, 2]]))
    print(sol.getSkyline([[1, 3, 2], [2, 4, 3], [5, 6, 2], [2, 5, 3]]))
    print(sol.getSkyline([[1, 4, 3]]))
    print(sol.getSkyline([[1, 4, 3], [2, 3, 2]]))
    print(sol.getSkyline([[1, 4, 3], [2, 3, 2], [5, 6, 2]]))
