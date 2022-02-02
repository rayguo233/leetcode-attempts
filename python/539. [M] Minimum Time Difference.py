from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted([int(s[:2]) * 60 + int(s[3:]) for s in timePoints])
        print(timePoints)
        res = 24 * 60 - timePoints[-1] + timePoints[0]
        for i in range(len(timePoints) - 1):
            res = min(res, timePoints[i + 1] - timePoints[i])
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    s = Solution()
    print(s.findMinDifference(["23:59","00:00"]))
