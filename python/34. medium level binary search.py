# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

LEFT, RIGHT = 0, 1

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def searchRangeHelper(nums: list[int], target: int, bound: int) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = int(left + (right - left) / 2)
                if nums[mid] == target:
                    if bound == LEFT: right = mid - 1
                    elif bound == RIGHT: left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if bound == LEFT and left < len(nums) and nums[left] == target: return left
            if bound == RIGHT and right >= 0 and nums[right] == target: return right
            return -1

        return [searchRangeHelper(nums, target, LEFT), searchRangeHelper(nums, target, RIGHT)]

if __name__ == '__main__':
    sol = Solution()
    assert(sol.searchRange([1,2,5], 2) == [1,1])
    assert(sol.searchRange([1,2,5], 0) == [-1,-1])
    print(sol.searchRange([1], 1))
    assert(sol.searchRange([1], 1) == [0,0])
    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
