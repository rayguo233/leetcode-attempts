import bisect
import collections
import heapq
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        res = 1
        for d in range(n):
            if d == 0:
                res *= 9
                continue
            res *= (10 - d)
        return res + self.countNumbersWithUniqueDigits(n - 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countNumbersWithUniqueDigits(4))
    print(sol.countNumbersWithUniqueDigits(2))
    print(sol.countNumbersWithUniqueDigits(3))
    # print(sol.nthSuperUglyNumber([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
