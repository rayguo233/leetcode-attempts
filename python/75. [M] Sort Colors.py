# https://leetcode-cn.com/problems/sort-colors/

# Given an array nums with n objects colored red,
# white, or blue, sort them in-place so that objects of
# the same color are adjacent, with the colors in the
# order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the
# color red, white, and blue, respectively.
#
# You must solve this problem without using the
# library's sort function.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-colors
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import random
from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums, start, end) -> None:
        l, r = start, end
        if l >= r:
            return
        pivot = nums[start]
        l += 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            while l < len(nums) and nums[l] <= pivot:
                l += 1
            while nums[r] > pivot:
                r -= 1
        nums[r], nums[start] = nums[start], nums[r]
        self.quick_sort(nums, start, r - 1)
        self.quick_sort(nums, r + 1, end)

    def sortColors_v0(self, nums: list[int]) -> None:
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort_v0(self, nums, l, r):
        if r - l <= 0:
            return
        # print(nums, l, r)
        pvt_i = self.partition(nums, l, r)
        # print(nums, pvt_i, l, r)
        self.quick_sort(nums, l, pvt_i - 1)
        self.quick_sort(nums, pvt_i + 1, r)

    def partition(self, nums, l, r) -> int:
        init_l = l
        pvt_i = random.randrange(start=l, stop=r + 1)
        pvt_val = nums[pvt_i]
        self.swap(nums, pvt_i, r)
        pvt_i = r
        r -= 1
        while l <= r:
            if nums[l] <= pvt_val:
                l += 1
            elif nums[r] < pvt_val:
                self.swap(nums, l, r)
                l += 1
                r -= 1
            else:
                r -= 1
        if nums[l] > pvt_val:
            self.swap(nums, l, pvt_i)
            return l
        return pvt_i

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


if __name__ == '__main__':
    sol = Solution()
    a = [2, 0]
    a = [0]
    a = [1, 2]
    a = [1, 0, 2]
    sol.sortColors(a)
    print(a)
    # print(sol.sortColors("a", 'aa'))
    # print(sol.minWindow_clean("ASDF", ''))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
