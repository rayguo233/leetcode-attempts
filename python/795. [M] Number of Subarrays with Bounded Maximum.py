import sys
from typing import List, Tuple

INDEX = int
NUM = int

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        stack_l = [(-1, sys.maxsize)]  # type: List[Tuple[INDEX, NUM]]
        stack_r = [(len(nums), sys.maxsize)]  # type: List[Tuple[INDEX, NUM]]
        right_num_min = [0] * len(nums)
        for i, num in enumerate(nums[::-1]):
            i = len(nums) - i - 1
            while stack_r[-1][1] < num:
                stack_r.pop()
            right_num_min[i] = stack_r[-1][0] - i
            stack_r.append((i, num))
        
        num_sub = 0
        for i, num in enumerate(nums):
            while stack_l[-1][1] <= num:
                stack_l.pop()
            left_num_min = i - stack_l[-1][0]
            stack_l.append((i, num))
            if not left <= num <= right:
                continue
            num_sub += left_num_min * right_num_min[i]

        return num_sub


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSubarrayBoundedMax([1,2,3,4,1,2,4,2], 2, 4))
    print(sol.numSubarrayBoundedMax([1], 2, 4))
