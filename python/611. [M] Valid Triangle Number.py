import bisect
from typing import List


class Solution:

    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        res = 0
        for i in range(length):
            if nums[i] == 0:
                continue
            for j in range(i + 1, length):
                sum_ij = nums[i] + nums[j]
                k = bisect.bisect_left(nums, sum_ij)
                # print(nums[i], nums[j], f'num choices: {k - j - 1}')
                res += k - j - 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.triangleNumber([0, 0, 0]))
    print(sol.triangleNumber([2, 1]))
    print(sol.triangleNumber([2, 2, 3, 4]))
    print(sol.triangleNumber([4, 2, 3, 4]))
