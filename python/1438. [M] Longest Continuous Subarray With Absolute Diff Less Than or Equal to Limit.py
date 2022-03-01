import collections
import heapq
from collections import OrderedDict
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap_removed = collections.defaultdict(int)
        max_heap_removed = collections.defaultdict(int)
        min_heap, max_heap = [nums[0]], [- nums[0]]
        l, r = 0, 0
        res = 1
        while True:
            while (r + 1 < len(nums)) and (- max_heap[0] - min_heap[0] <= limit):
                res = max(res, r - l + 1)
                r += 1
                heapq.heappush(min_heap, nums[r])
                heapq.heappush(max_heap, - nums[r])

            while (l < r) and (- max_heap[0] - min_heap[0] > limit):
                min_heap_removed[nums[l]] += 1
                max_heap_removed[nums[l]] += 1
                while min_heap_removed[min_heap[0]]:
                    min_heap_removed[min_heap[0]] -= 1
                    heapq.heappop(min_heap)
                while max_heap_removed[- max_heap[0]]:
                    max_heap_removed[- max_heap[0]] -= 1
                    heapq.heappop(max_heap)
                l += 1

            if r == len(nums) - 1:
                return max(res, r - l + 1)





if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubarray([2,1,4], 4))
    print(sol.longestSubarray([2,1,4,1],1))
    print(sol.longestSubarray([2,1,4,1],0))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
