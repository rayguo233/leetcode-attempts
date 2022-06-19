# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size
# m and n respectively, return the median of the
# two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List, Optional

INF = 10**7


class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        nums1 = [-INF - 1, -INF] + nums1 + [INF, INF + 1]
        nums2 = [-INF - 1, -INF] + nums2 + [INF, INF + 1]
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m - 1
        i = (lo + hi) // 2
        j = self.get_j_from_i(i, m, n)
        while not self.is_median_found(i, j, nums1, nums2):
            if nums1[i] < nums2[j]:
                lo = i + 1
            else:
                hi = i - 1
            i = (lo + hi) // 2
            j = self.get_j_from_i(j, m, n)
        print('------', i, j, nums1[i], nums2[j])
        return self.get_median(i, j, nums1, nums2)

    def get_j_from_i(self, i, m, n) -> int:
        return ((m + n + 1) // 2) - i - 2

    def is_median_found(self, i, j, nums1, nums2) -> bool:
        m, n = len(nums1), len(nums2)
        if nums2[j] == -INF:
            return nums2[j + 1] == INF or nums1[i - 1] > nums2[j + 1]
        if nums2[j] == INF:
            return nums2[j - 1] == -INF or nums1[i - 1] > nums2[j + 1]
        return nums1[i - 1] <= nums2[j] <= nums1[i + 1] and nums2[
            j - 1] <= nums1[i] <= nums2[j + 1]

    def get_median(self, i, j, nums1, nums2) -> int:
        if (len(nums1) + len(nums2)) % 2:
            return max(nums1[i], nums2[j])
        if nums1[i] <= -INF or nums1[i] >= INF:
            return sum(nums2[j:j + 2]) / 2.
        if nums2[j] <= -INF or nums2[j] >= INF:
            return sum(nums1[i:i + 2]) / 2.
        return (nums1[i] + nums2[j]) / 2.


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))
    print(sol.findMedianSortedArrays([1, 2, 3], [4]))
    print(sol.findMedianSortedArrays([1, 2, 3], [0]))
    print(sol.findMedianSortedArrays([1, 2], []))
    print(sol.findMedianSortedArrays([1], []))
    print(sol.findMedianSortedArrays([], [1]))
