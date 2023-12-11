from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        tails = self.subsetsWithDup(nums[1:])
        return tails + [[nums[0]] + tail for tail in tails]


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup([1,2,3]))