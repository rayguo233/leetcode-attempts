import bisect
import collections
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        tuples = sorted([(val, key) for key, val in d.items()], reverse=True)
        return ''.join([key * val for val, key in tuples])


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort('asdfsadffgfds'), -1)
