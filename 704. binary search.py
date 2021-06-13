# https://leetcode-cn.com/problems/binary-search/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    assert(sol.search([1,2,5], 2) == 1)
    assert(sol.search([1,2,5], 0) == -1)
    assert(sol.search([1], 1) == 0)
    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
