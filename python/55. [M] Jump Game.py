# https://leetcode.com/problems/jump-game/

# YGiven an array of non-negative integers nums, you
# are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum
# jump length at that position.
#
# Determine if you are able to reach the last index.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        target = len(nums) - 1
        maxi = 0
        for i, num in enumerate(nums):
            if i > maxi: break
            maxi = max(maxi, i + num)
        return maxi >= target

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(2, [3,2,6,5,0,3]))
