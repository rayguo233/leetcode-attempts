import bisect
import collections
import heapq
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [1]
        candidates = [(prime * ugly_nums[0], prime, 0) for prime in primes]
        heapq.heapify(candidates)
        while len(ugly_nums) < n:
            ugly_num, prime, i = heapq.heappop(candidates)
            if ugly_num != ugly_nums[-1]:
                ugly_nums.append(ugly_num)
            heapq.heappush(candidates, (prime * ugly_nums[i+1], prime, i+1))
        return ugly_nums[n-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))
    # print(sol.nthSuperUglyNumber([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
