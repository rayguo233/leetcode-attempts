# https://leetcode-cn.com/problems/3sum/

# Given an array of integers nums and an integer
# target, return indices of the two numbers such
# that they add up to target.
#
# You may assume that each input would have exactly
# one solution, and you may not use the same element
# twice.
#
# You can return the answer in any order.。

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        record = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in record:
                return [i, record[need]]
            record[num] = i

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([1,2,4,7,5,0], 1))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
