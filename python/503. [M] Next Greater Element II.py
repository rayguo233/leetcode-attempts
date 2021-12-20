# https://leetcode.com/problems/next-greater-element-ii/
from typing import List, Tuple


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = []  # type: List[Tuple[int, int]]
        for i, num in enumerate(nums):
            while stack and num > stack[-1][1]:
                res[stack[-1][0]] = num
                stack.pop()
            stack.append((i, num))

        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                res[stack[-1][0]] = num
                stack.pop()
            if not stack:
                break

        for i, num in stack:
            res[i] = -1

        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([1,2,3,2,1]))
    # assert(sol.invertTree([1,2,1,2]) == 1)
