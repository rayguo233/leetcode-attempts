import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int: pass
   def length(self) -> int: pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        memo = {}
        def find(i) -> int:
            if i not in memo:
                memo[i] = mountain_arr.get(i)
            return memo[i]
        l, r = 0, mountain_arr.length() - 1
        cand = [(l, r)]
        res = []
        while cand and len(res) < 2:
            print(cand)
            l, r = cand.pop()
            if l > r:
                continue
            mid = (l + r) // 2
            mid_val = find(mid)
            if mid_val == target:
                res.append(mid)
                continue
            if mid == 0:
                cand.append((mid + 1, r))
                continue
            if mid == mountain_arr.length() - 1:
                cand.append((l, mid - 1))
                continue
            mid_left_val, mid_right_val = find(mid-1), find(mid+1)
            left_val, right_val = find(l), find(r)
            if (mid_left_val < mid_val and left_val <= target < mid_val) or\
               (mid_left_val > mid_val and (left_val <= target or mid_val < target)):
                    cand.append((l, mid - 1))
            if (mid_right_val < mid_val and right_val <= target < mid_val) or\
               (mid_right_val > mid_val and (right_val <= target or mid_val < target)):
                    cand.append((mid + 1, r))
        return -1 if not res else min(res)






if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2(100, 50, [[25,30]]), -1)
