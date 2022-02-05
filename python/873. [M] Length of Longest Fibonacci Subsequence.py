import bisect
import collections
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        d = {num: i for i, num in enumerate(arr)}
        curr = []
        for i, a in enumerate(arr):
            for j in range(i + 1, len(arr)):
                b = arr[j]
                curr.append((b, a + b))
        level = 2
        while curr:
            print(curr)
            next_arr = []
            found = False
            for b, c in curr:
                if c not in d:
                    continue
                found = True
                next_arr.append((c, b + c))
            level += found
            curr = next_arr
        return level if level > 2 else 0




if __name__ == '__main__':
    sol = Solution()
    print(sol.lenLongestFibSubseq([1,2,3,4,5,6,7,8]), 5)
    print(sol.lenLongestFibSubseq([1,3,7,11,12,14,18]), 3)
