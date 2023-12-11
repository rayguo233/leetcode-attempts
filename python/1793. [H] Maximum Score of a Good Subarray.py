import bisect
import sys
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        num_left, num_right = k + 1, len(nums) - k
        dp = [[sys.maxsize] * num_right for _ in range(num_left)]
        left_dis = 0
        res = 0
        for right_dis in range(num_right):
            if right_dis == 0:
                dp[left_dis][right_dis] = nums[k]
                res = nums[k]
                continue
            dp[left_dis][right_dis] = min(dp[left_dis][right_dis-1], nums[k+right_dis])
            res = max(res, (right_dis + left_dis + 1) * dp[left_dis][right_dis])
        for left_dis in range(1, num_left):
            for right_dis in range(num_right):
                dp[left_dis][right_dis] = min(dp[left_dis-1][right_dis], nums[k - left_dis])
                res = max(res, (right_dis + left_dis + 1) * dp[left_dis][right_dis])
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumScore(nums = [1,4,3,7,4,5], k = 3), 15)
    print(sol.maximumScore(nums = [5,5,4,5,4,1,1,1], k = 0), 20)
