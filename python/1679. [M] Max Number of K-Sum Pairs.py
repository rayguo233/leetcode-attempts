import bisect
import collections
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        res = 0
        for num in nums:
            if d[k-num]:
                d[k-num] -= 1
                res += 1
                continue
            d[num] += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxOperations([1,2,3,4], 5))