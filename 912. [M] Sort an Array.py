# https://leetcode-cn.com/problems/sort-an-array/

# YGiven an array of integers nums, sort the array
# in ascending order.

class Solution:
    def sortArray_quick_sort(self, nums: list[int]) -> list[int]:
        self.quick_sort(nums, 0, len(nums)-1)
        return nums

    def quick_sort(self, nums, l, r):
        if r - l <= 0: return
        pvt = self.partition(nums, 0, r)
        self.quick_sort(nums, 0, pvt - 1)
        self.quick_sort(nums, pvt + 1, r)

    def partition(self, nums, l, r) -> int:
        p = r
        pvt = nums[r]
        while l < r:
            if nums[l] <= pvt: l += 1
            elif nums[r] < pvt:
                self.swap(nums, l, r)
                l, r = l+1, r-1
            else: r -= 1
        if l < p: self.swap(nums, l, p)
        return l

    def swap(self, nums, a, b):
        # print(nums, a, b)
        nums[a], nums[b] = nums[b], nums[a]

if __name__ == '__main__':
    sol = Solution()
    a = [1,2,3,2,5,2,4]
    sol.sortArray_quick_sort(a)
    print(a)
