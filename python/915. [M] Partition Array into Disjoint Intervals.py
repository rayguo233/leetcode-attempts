
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        mins = nums.copy()
        for i, num in enumerate(reversed(nums[:-1]), start = 2):
            mins[-i] = min(num, mins[-i+1])
        res = 1
        curr_max = nums[0]
        if curr_max < mins[1]:
            return 1
        for i, num in enumerate(nums[1:-1], start=1):
            curr_max = max(num, curr_max)
            if curr_max <= mins[i+1]:
                return i + 1
#        print(mins)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionDisjoint([1,2]))
    print(sol.partitionDisjoint([1,2,10,9,20]))
    print(sol.partitionDisjoint([1,1,1,0,6,12]))
    print(sol.partitionDisjoint([1,2]))
    print(sol.partitionDisjoint([1,2]))
    pass