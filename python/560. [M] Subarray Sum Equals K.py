# https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k,
# return the total number of continuous subarrays
# whose sum equals to k.

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

from collections import defaultdict

class Solution:
    def subarraySum_too_slow(self, nums: list[int], k: int) -> int:
        res = 0
        stack = []

        for n in nums:
            new_stack = []
            for a in stack:
                if a + n == k: res += 1
                new_stack.append(a + n)
            if n == k: res += 1
            new_stack.append(n)
            stack = new_stack
        return res

    def subarraySum(self, nums: list[int], k: int) -> int:
        presum = defaultdict(int)
        presum[0] += 1
        currsum = 0
        res = 0
        for n in nums:
            currsum += n
            if currsum - k in presum:
                res += presum[currsum - k]
            presum[currsum] += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraySum(nums=[1,1,1], k=2))
    print(sol.subarraySum(nums=[1,2,3], k=3))
