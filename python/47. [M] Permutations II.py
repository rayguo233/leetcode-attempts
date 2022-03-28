from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        used = [False] * n
        res = []
        self.dfs(nums, used, [], res)
        return res

    
    def dfs(self, nums: List[int], used: List[int], arr: List[int], res: List[List[int]]) -> None:
        if len(arr) == len(nums):
            res.append(arr.copy())
            return
        prev_used = -100
        for i, num in enumerate(nums):
            if used[i] or num == prev_used:
                continue
            arr.append(num)
            used[i] = True
            self.dfs(nums, used, arr, res)
            arr.pop()
            used[i] = False
            prev_used = num


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1,1,2]))
    print(sol.permuteUnique([1,1,2,2]))