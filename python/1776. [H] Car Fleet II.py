import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        res = [[-1., None] for _ in cars]
        for i in reversed(range(len(cars) - 1)):
            pos_i, speed_i = cars[i]
            res_i = [-1., None]
            j = i + 1
            while j and j < len(cars):
                pos_j, speed_j = cars[j]
                if speed_j >= speed_i:
                    j = res[j][1]
                    continue
                time = float(pos_j - pos_i) / (speed_i - speed_j)
                if time < res[j][0] or res[j][1] is None:
                    res_i = [time, j]
                    break
                j = res[j][1]
            res[i] = res_i

        # print(res)

        return [ans for ans, _ in res]

if __name__ == '__main__':
    sol = Solution()
    print(sol.getCollisionTimes([[2,1]]))
    print(sol.getCollisionTimes([[1,2],[2,1],[4,3],[7,2]]))
    print(sol.getCollisionTimes([[3,4],[5,4],[6,3],[9,1]]))
    # print(sol.isNStraightHand([2,1,4,7,3,2,5,6], 2) == True)
    # print(sol.isNStraightHand([2,1], 2) == True)
    # print(sol.isNStraightHand([2,1], 1) == True)
    # print(sol.isNStraightHand([3,1], 2) == False)
