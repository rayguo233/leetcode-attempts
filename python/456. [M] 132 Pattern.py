from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        left = nums[0]
        for i in range(1, n - 1):
            mid = nums[i]
            if mid <= left:
                left = mid
                continue
            for right in nums[i+1:]:
                if left < right < mid:
                    return True
            
        return False
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.find132pattern([1,2,3]))
    print(sol.find132pattern([1,2,3,2]))
    print(sol.find132pattern([1,4,3]))
