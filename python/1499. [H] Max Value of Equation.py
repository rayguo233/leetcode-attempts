import heapq
from typing import List, Tuple
import collections


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = -float('inf')
        hp = []  # type: List[Tuple[int, int]]
        for xj, yj in points:
            # print(xj, yj, hp)
            while hp:
                yi_minus_xi, xi = hp[0]
                yi_minus_xi, xi = -yi_minus_xi, -xi
                if xj - xi > k:
                    heapq.heappop(hp)
                    continue
                res = max(res, xj + yj + yi_minus_xi)
                break
            heapq.heappush(hp, (xj - yj, - xj))
        return res

if __name__ == '__main__':
    sol = Solution()
    # print(sol.largestNumber([1,2,3,4,5,6,7,8,9], 11))
    # print(sol.largestNumber([4,3,2,5,6,7,2,5,5],9))
    print(sol.findMaxValueOfEquation([[-19,1],[-18,-13],[-17,-12],[-14,-14],[-8,-9],[-6,16],[-2,-4],[2,15],[4,19],[5,-9],[6,20],[7,-17],[16,3]],
            5))
    # assert(sol.rob([2,1,4]) == 6)
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 10)
    # assert(sol.rob([2,1,4,8,9]) == 15)
