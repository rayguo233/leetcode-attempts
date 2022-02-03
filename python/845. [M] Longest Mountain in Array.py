import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        len_arr = len(arr)
        if len_arr < 3:
            return 0
        res = 0
        mid = 1
        while mid < len_arr - 1:
            if not (arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]):
                mid += 1
                continue
            l, r = mid, mid
            while 0 <= l - 1 and arr[l-1] < arr[l]:
                l -= 1
            while r + 1 < len_arr and arr[r] > arr[r+1]:
                r += 1
            res = max(res, r - l + 1)
            mid = r + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestMountain([2,1,4,7,3,2,5]))
    print(sol.longestMountain([2,2,2]))
