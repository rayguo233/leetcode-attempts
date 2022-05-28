import collections
from typing import List


class Solution:

    def countNicePairs(self, nums: List[int]) -> int:

        def rev(a: int) -> int:
            return int(str(a)[::-1])

        counter = collections.Counter(num - rev(num) for num in nums)
        return int(
            sum(((freq - 1) * freq / 2) % (10**9 + 7)
                for freq in counter.values()) % (10**9 + 7))


if __name__ == '__main__':
    sol = Solution()
    print(sol.countNicePairs([232, 543, 123, 543]))
    print(sol.countNicePairs([42, 11, 1, 97]))
    print(sol.countNicePairs([13, 10, 35, 24, 76]))
