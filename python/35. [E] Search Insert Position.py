from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid       
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1,3,5], 2))
    print(sol.searchInsert([1,3,5], 6))
    print(sol.searchInsert([1,3,5], 0))
    print(sol.searchInsert([1], 0),0)
    print(sol.searchInsert([1], 2),1)
    print(sol.searchInsert([1], 1),0)
    print(sol.searchInsert([1,3,5], 5),2)