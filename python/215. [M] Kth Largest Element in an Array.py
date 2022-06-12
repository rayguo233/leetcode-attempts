from typing import List, Optional


class Solution:

    def findKthLargest(self,
                       nums: List[int],
                       k: int,
                       start=0,
                       end=None) -> Optional[int]:
        index_k = len(nums) - k
        if end is None:
            end = len(nums) - 1
        assert start <= end
        if start == end:
            assert index_k == start
            return nums[start]
        pivot = nums[start]
        l, r = start + 1, end
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            while l <= end and nums[l] <= pivot:
                l += 1
            while nums[r] > pivot:
                r -= 1
        nums[r], nums[start] = nums[start], nums[r]
        if r == index_k:
            return pivot
        if r < index_k:
            return self.findKthLargest(nums, k, r + 1, end)
        return self.findKthLargest(nums, k, start, r - 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 4))
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 5))
