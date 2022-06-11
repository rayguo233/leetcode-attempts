from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        ans = float('inf')
        for left_i, left in enumerate(nums):
            if left_i > 0 and nums[left_i] == nums[left_i - 1]:
                continue
            mid_i, right_i = left_i + 1, length - 1
            while mid_i < right_i:
                mid, right = nums[mid_i], nums[right_i]
                curr_sum = left + mid + right
                if abs(target - curr_sum) < abs(target - ans):
                    ans = curr_sum
                if curr_sum <= target:
                    mid_i += 1
                    while mid_i < length and nums[mid_i] == nums[mid_i - 1]:
                        mid_i += 1
                else:
                    right_i -= 1
                    while right_i > 0 and nums[right_i] == nums[right_i + 1]:
                        right_i -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(sol.threeSum_try2([-1,-1,1,2,-1,-3]))
    # assert(sol.threeSum_try2([-1,-1,1,2,-1,-1]) == [[-1,-1,2]])
    # assert(sol.threeSum_try2([1]) == [])
    # assert(sol.threeSum_try2([1,2]) == [])
    # assert(sol.threeSum_try2([]) == [])
