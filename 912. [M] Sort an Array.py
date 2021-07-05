# https://leetcode-cn.com/problems/sort-an-array/

# YGiven an array of integers nums, sort the array
# in ascending order.

import random


class Solution:
    def sortArray_qs(self, nums: list[int]) -> list[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, l, r):
        if r - l <= 0: return
        pvt = self.partition(nums, l, r)
        self.quick_sort(nums, l, pvt - 1)
        self.quick_sort(nums, pvt + 1, r)

    def partition(self, nums, l, r) -> int:
        p = random.randrange(l, r + 1)
        self.swap(nums, p, r)
        p = r
        pvt = nums[r]
        r -= 1
        while l <= r:
            if nums[l] <= pvt:
                l += 1
            elif nums[r] <= pvt:
                self.swap(nums, l, r)
                l, r = l + 1, r - 1
            else:
                r -= 1
        if l < p:
            self.swap(nums, l, p)
        return min(l, p)

    def swap(self, nums, a, b):
        # print(nums, a, b)
        nums[a], nums[b] = nums[b], nums[a]

if __name__ == '__main__':
    sol = Solution()
    a = [-4,0,7,4,9,-5,-1,0,-7,-1]
    a = [5,2,3,1]
    sol.sortArray_qs(a)
    print(a)
