from heapq import nlargest, nsmallest
from typing import List


class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        largest_4 = nlargest(4, nums)
        smallest_4 = nsmallest(4, nums)
        diff_1, diff_2 = [0] * 3, [0] * 3
        for i in range(3):
            diff_1[i] = largest_4[i] - largest_4[i + 1]
            diff_2[i] = smallest_4[i + 1] - smallest_4[i]
        print(largest_4, smallest_4)
        print(diff_1, diff_2)
        max_diff = largest_4[0] - smallest_4[0]
        res = max_diff
        for i in range(0, 4):
            res = min(res, max_diff - sum(diff_1[:i]) - sum(diff_2[:(3 - i)]))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDifference([1, 4, 5, 7, 10]))
    print(sol.minDifference([6, 6, 0, 1, 1, 4, 6]))
