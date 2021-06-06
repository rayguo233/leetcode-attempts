# https://leetcode-cn.com/problems/permutations/

# Given an array nums of distinct integers, return all
# the possible permutations. You can return the answer in any order.

INF = float('inf')

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]

        res = []  # type: list[list[int]]
        
        for i, num in enumerate(nums):
            # print(i, num, nums)
            sub_perms = self.permute(nums[:i] + nums[i+1:])  # type: list[list[int]]
            # print(sub_perms)
            for sub_perm in sub_perms:
                sub_perm.append(num)
                res.append(sub_perm)

        return res




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1,2,5,3]))
    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)