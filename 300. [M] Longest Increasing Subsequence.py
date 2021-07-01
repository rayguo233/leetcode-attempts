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

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
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
    # print(sol.maxProfit(2, [3,2,6,5,0,3]))
