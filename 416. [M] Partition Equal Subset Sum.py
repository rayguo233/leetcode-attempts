# https://leetcode-cn.com/problems/partition-equal-subset-sum/

# Given a non-empty array nums containing only positive
# integers, find if the array can be partitioned into
# two subsets such that the sum of elements in both
# subsets is equal.
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False

        target = int(summ / 2)
        dp = [False] * (target + 1)  # type: list[bool]
        dp[0] = True

        for num in nums:
            for i in range(target, 0, -1):
                if dp[i] or i - num < 0:
                    continue
                dp[i] = dp[i - num]
            if dp[target]:
                return True
            print(dp)
        return dp[target]






if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([1,2,5]))
    # print(sol.canPartition('cbaebabacd', "abc"))
