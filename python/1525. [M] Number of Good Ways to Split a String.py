import bisect
import collections
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def numSplits(self, s: str) -> int:
        len_s = len(s)
        left_distinct, right_distinct = [1] * len_s, [1] * len_s
        d = collections.defaultdict(int)
        for i, c in enumerate(s):
            d[c] += 1
            left_distinct[i] = len(d)
        d.clear()
        for i, c in enumerate(reversed(s)):
            i = len_s - i - 1
            d[c] += 1
            right_distinct[i] = len(d)
        res = 0
        for i in range(0, len_s - 1):
            res += (left_distinct[i] == right_distinct[i + 1])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.racecar(1), 1)
    print(sol.racecar(2), 4)
    print(sol.racecar(3), 2)
    print(sol.racecar(6))
