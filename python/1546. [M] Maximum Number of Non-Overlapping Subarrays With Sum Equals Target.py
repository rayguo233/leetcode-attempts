import itertools
from typing import List


class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sums = {}
        res = 0
        for num in nums:
            if num == target:
                res += 1
                sums = {}
                continue
            next_sums = set()
            for sub_sum in itertools.chain(sums, [0]):
                if sub_sum + num == target:
                    res += 1
                    next_sums = {}
                    break
                else:
                    next_sums.add(sub_sum + num)
            sums = next_sums
        return res


if __name__ == '__main__':
    pass
    sol = Solution()
    print(sol.maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]))
