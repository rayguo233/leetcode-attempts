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

    def sortArray_ms(self, nums: list[int]) -> list[int]:
        arr = [0] * len(nums)
        last = len(nums) -1
        self.mergesort(nums, 0, last, arr)
        # self.merge(nums, arr, 0, last // 2, last // 2 + 1, last)
        return nums

    def mergesort(self, nums, l, r, arr):
        if r <= l:
            return
        mid = (l + r) // 2
        self.mergesort(nums, l, mid, arr)
        self.mergesort(nums, mid+1, r, arr)
        if nums[mid] > nums[mid+1]:
            self.merge(nums, arr, l, mid, mid+1, r)
        print(nums, l, mid, r)

    def merge(self, nums, arr, l1, r1, l2, r2):
        start, end = l1, r2
        ptr = l1
        while l1 <= r1 and l2 <= r2:
            if nums[l1] <= nums[l2]:
                arr[ptr] = nums[l1]
                l1 += 1
            else:
                arr[ptr] = nums[l2]
                l2 += 1
            ptr += 1
        while l1 <= r1:
            arr[ptr] = nums[l1]
            l1 += 1
            ptr += 1
        while l2 <= r2:
            arr[ptr] = nums[l2]
            l2 += 1
            ptr += 1
        nums[start:end+1] = arr[start:end+1]
        # print(nums, arr)

if __name__ == '__main__':
    sol = Solution()
    a = [-4,0,7,4,9,-5,-1,0,-7,-1]
    a = [5,2,3,1]
    sol.sortArray_ms(a)
    print(a)
