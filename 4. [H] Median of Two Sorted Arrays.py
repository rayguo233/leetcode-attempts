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

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        imin, imax = 0, m - 1
        i = (imin + imax) // 2
        j = ((m + n) // 2) - i - 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('sdffssdfgghjk'))
    print(sol.lengthOfLongestSubstring('sdfsdfs'))
    print(sol.lengthOfLongestSubstring(''))
