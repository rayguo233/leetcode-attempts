# https://leetcode-cn.com/problems/3sum/

# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# 0 <= nums.length
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        ptr = 0
        n = len(nums)

        # set the first ptr in each loop
        while ptr < n and nums[ptr] <= 0:
            l, r = ptr + 1, n - 1
            while l < r:
                # if result found
                if nums[l] + nums[r] == - nums[ptr]:
                    res.append([nums[ptr], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1

                # if twoSum too small
                elif nums[l] + nums[r] < - nums[ptr]:
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1

                # if twoSUm too large
                elif nums[l] + nums[r] > - nums[ptr]:
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1

            # skip through duplicates
            while ptr + 1 < n and nums[ptr] == nums[ptr + 1]:
                ptr += 1
            ptr += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1,-1,1,2,-1,-3]))
    print(sol.threeSum([-1,-1,1,2,-1,-1]) == [[-1,-1,2]])
    print(sol.threeSum([1]) == [])
    assert(sol.threeSum([1,2]) == [])
    assert(sol.threeSum([]) == [])
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
