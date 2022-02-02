import functools
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        def cmp(a: str, b: str) -> int:
            ab, ba = a + b, b + a
            if ab == ba: return 0
            if ab < ba: return -1
            return 1
        nums = sorted(nums, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(nums)



if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([432, 43243]))
    print(sol.largestNumber([0,1,11,12,24,21,98,9,94,2]))
