# https://leetcode-cn.com/problems/longest-increasing-subsequence/

# Given an integer array nums, return the length of the longest
# strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array
# by deleting some or no elements without changing the order of
# the remaining elements. For example, [3,6,2,7] is a subsequence
# of the array [0,3,1,6,2,2,7].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import bisect
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        len_to_last = [float('inf')] * len(nums)
        max_len = 0
        for num in nums:
            index = bisect.bisect_left(len_to_last, num, hi=max_len)
            len_to_last[index] = min(num, len_to_last[index])
            max_len = max(max_len, index + 1)
        return max_len

    def lengthOfLIS_v0(self, nums: list[int]) -> int:
        if not nums: return 0
        res = 1
        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            maxi = 1
            for j, prev in enumerate(nums[:i]):
                if prev < num: maxi = max(maxi, dp[j] + 1)
            dp[i] = maxi
            res = max(res, maxi)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([1, 2, 3, 4]))
    print(sol.lengthOfLIS([1, 0, 3, 4]))
    print(sol.lengthOfLIS([4, 0, 3, 2]))
    print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
