# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such
# that answer[i] is equal to the product of all the elements
# of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed
# to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and
# without using the division operation.

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed
# to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left, right = [1] * len(nums), [1] * len(nums)
        left[0] = nums[0]
        for i, n in enumerate(nums[1:], start=1):
            left[i] = left[i-1] * n
        right[-1] = nums[-1]
        for i, n in reversed(list(enumerate(nums[:-1]))):
            right[i] = right[i+1] * n
        res = [1] * len(nums)
        res[0] = right[1]
        res[-1] = left[-2]
        for i in range(1, len(nums)-1):
            res[i] = left[i-1] * right[i+1]
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([-1,1,0,-3,3]))
    # print(sol.productExceptSelf('sdfsdfs'))
    # print(sol.productExceptSelf(''))
#