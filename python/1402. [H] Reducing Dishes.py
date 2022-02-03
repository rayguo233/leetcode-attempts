import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        first_pos_i = bisect.bisect_left(satisfaction, 0)
        neg, pos = satisfaction[:first_pos_i], satisfaction[first_pos_i:]
        res = 0
        pos_sum = 0
        for i, p in enumerate(pos):
            pos_sum += p
            res += (i + 1) * p
        for n in reversed(neg):
            if pos_sum + n > 0:
                pos_sum += n
                res += pos_sum
            else:
                break
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSatisfaction([0,5,3,1,-2]))
