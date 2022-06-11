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

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)
        for left_i, left in enumerate(nums):
            if left_i > 0 and nums[left_i - 1] == left:
                continue
            mid_i, right_i = left_i + 1, length - 1
            while mid_i < right_i:
                mid, right = nums[mid_i], nums[right_i]
                if left + mid + right <= 0:
                    if left + mid + right == 0:
                        res.append([left, mid, right])
                    mid_i += 1
                    while mid_i < length and nums[mid_i] == nums[mid_i - 1]:
                        mid_i += 1
                else:
                    right_i -= 1
                    while right_i >= 0 and nums[right_i] == nums[right_i + 1]:
                        right_i -= 1
        return res

    def threeSum_v0(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        ptr = 0
        n = len(nums)

        # set the first ptr in each loop
        while ptr < n and nums[ptr] <= 0:
            l, r = ptr + 1, n - 1
            while l < r:
                # if result found
                if nums[l] + nums[r] == -nums[ptr]:
                    res.append([nums[ptr], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1

                # if twoSum too small
                elif nums[l] + nums[r] < -nums[ptr]:
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1

                # if twoSUm too large
                elif nums[l] + nums[r] > -nums[ptr]:
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1

            # skip through duplicates
            while ptr + 1 < n and nums[ptr] == nums[ptr + 1]:
                ptr += 1
            ptr += 1

        return res

    def threeSum_try2(self, nums: list[int]) -> list[list[int]]:

        def skip_duplicates(start, direction, leng) -> int:
            curr = nums[start]
            while leng > start > 0 and nums[start] == curr:
                start = start + direction
            return start

        LEFT, RIGHT = -1, 1
        leng = len(nums)
        if leng < 3: return []
        res = []
        nums.sort()
        first = 0

        while first < leng - 2:
            second, third = first + 1, leng - 1
            while second < third:
                summ = nums[first] + nums[second] + nums[third]
                if summ == 0:
                    res.append([nums[first], nums[second], nums[third]])
                    second = skip_duplicates(second, RIGHT, leng)
                    third = skip_duplicates(third, LEFT, leng)
                elif summ < 0:
                    second += 1
                else:
                    third -= 1
            curr = nums[first]
            # move the first pointer skipping duplicate values
            while first < leng and nums[first] == curr:
                first += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(sol.threeSum_try2([-1,-1,1,2,-1,-3]))
    # assert(sol.threeSum_try2([-1,-1,1,2,-1,-1]) == [[-1,-1,2]])
    # assert(sol.threeSum_try2([1]) == [])
    # assert(sol.threeSum_try2([1,2]) == [])
    # assert(sol.threeSum_try2([]) == [])
