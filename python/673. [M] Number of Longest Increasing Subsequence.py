import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in nums]
        max_len = 1
        for i, num in enumerate(nums):
            valid_prev_i = [prev_i for prev_i, prev in enumerate(nums[:i]) if prev < num]
            dp[i][0] = max([dp[prev_i][0] + 1 for prev_i in valid_prev_i] or [1])
            dp[i][1] = sum([dp[prev_i][1] for prev_i in valid_prev_i if dp[prev_i][0] == (dp[i][0] - 1)] or [1])
            max_len = max(dp[i][0], max_len)
        return sum(freq for leng, freq in dp if leng == max_len)

        

if __name__ == '__main__':
    sol = Solution()
    print(sol.findNumberOfLIS([25,30]), 1)
    print(sol.findNumberOfLIS([25,30,26]), 2)
    print(sol.findNumberOfLIS([25,3,1]), 3)
    print(sol.findNumberOfLIS([1,3,5,4,7]), 2)
    print(sol.findNumberOfLIS([1,2,4,3,5,4,7,2]), 3)
