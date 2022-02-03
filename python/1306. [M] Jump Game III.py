import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        next = [start]
        visited = {start}
        len_arr = len(arr)
        while next:
            i = next.pop()
            val = arr[i]
            if val == 0:
                return True
            for j in (i + val, i - val):
                if not (0 <= j < len_arr) or j in visited:
                    continue
                if arr[j] == 0:
                    return True
                visited.add(j)
                next.append(j)
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canReach(arr = [3,0,2,1,2], start = 2))
