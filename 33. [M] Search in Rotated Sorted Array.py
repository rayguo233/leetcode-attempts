# https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order
# (with distinct values).
#
# Prior to being passed to your function, nums is rotated at
# an unknown pivot index k (0 <= k < nums.length) such that
# the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
# nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example,
# [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
# [4,5,6,7,0,1,2].
#
# Given the array nums after the rotation and an integer
# target, return the index of target if it is in nums, or
# -1 if it is not in nums.
#
# 1 <= nums.length
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums[-1] == target:
            return r
        while l < r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            # if mid and target on the same side
            if ((nums[m] - nums[-1]) * (target - nums[-1])) >= 0:
                if target < nums[m]:
                    r = m
                else:
                    l = m + 1
            # else mid and target on different side
            else:
                if target < nums[m]:
                    l = m + 1
                else:  # target > nums[m]
                    r = m
        assert (l == r)
        return l if nums[l] == target else -1





if __name__ == '__main__':
    sol = Solution()
    # print(sol.search([4,5,6,7,0,1,2], 3))
    # print(sol.search([4, 5], 4))
    print(sol.search([1,3,5], 1))
    # assert(sol.invertTree([1,2,1,2]) == 1)
