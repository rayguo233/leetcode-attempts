from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i1, num1 in enumerate(nums):
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            for i2, num2 in enumerate(nums[i1 + 1:], start=i1 + 1):
                if i2 > i1 + 1 and nums[i2] == nums[i2 - 1]:
                    continue
                i3, i4 = i2 + 1, len(nums) - 1
                while i3 < i4:
                    num3, num4 = nums[i3], nums[i4]
                    curr_sum = num1 + num2 + num3 + num4
                    if curr_sum <= target:
                        if curr_sum == target:
                            res.append([num1, num2, num3, num4])
                        i3 += 1
                        while i3 < len(nums) and nums[i3] == nums[i3 - 1]:
                            i3 += 1
                    else:
                        i4 -= 1
                        while i4 > 0 and nums[i4] == nums[i4 + 1]:
                            i4 -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(sol.threeSum_try2([-1,-1,1,2,-1,-3]))
    # assert(sol.threeSum_try2([-1,-1,1,2,-1,-1]) == [[-1,-1,2]])
    # assert(sol.threeSum_try2([1]) == [])
    # assert(sol.threeSum_try2([1,2]) == [])
    # assert(sol.threeSum_try2([]) == [])
