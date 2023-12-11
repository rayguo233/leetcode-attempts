from functools import lru_cache
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        arr = nums
        d = {}

        def find_subseq_from_i(prev: int, i: int) -> List[List[int]]:
            if i in d:
                return d[i]
            res = [[arr[i]]]
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    continue
                res += [[arr[i]] + subseq for subseq in find_subseq_from_i(arr[i], j)]
            d[(prev, i)] = res
            return res
        
        res = []
        for i in range(len(nums)):
            res += [subseq for subseq in find_subseq_from_i(-200, i) if len(subseq) > 1]
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubsequences([1,1,1]))