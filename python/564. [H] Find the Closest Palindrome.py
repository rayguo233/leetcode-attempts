# https://leetcode-cn.com/problems/permutation-in-string/

# Given two strings s1 and s2, return true if s2 contains the permutation of s1.
#
# In other words, one of s1's permutations is the substring of s2.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutation-in-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict
from math import floor, ceil


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        candidates = []  # type: List
        mid_i_floor, mid_i_ceil = floor(len(n) / 2), ceil(len(n) / 2)
        cand = n[:mid_i_ceil] + n[:mid_i_floor][::-1]
        candidates.append(cand)
        mid_char = n[mid_i_floor] if mid_i_floor != mid_i_ceil else n[mid_i_floor-1]
        if mid_char != '9':
            if mid_i_floor == mid_i_ceil:
                candidates.append(n[:mid_i_floor-1] + 2*str(int(mid_char)+1) + n[:mid_i_floor-1][::-1])
            else:
                candidates.append(n[:mid_i_floor] + str(int(mid_char)+1) + n[:mid_i_floor][::-1])
        if cand == n:
            if mid_char != '0':
                mid_char = str(int(mid_char) - 1)
            else:
                mid_char = '1'
            if mid_i_floor == mid_i_ceil:
                candidates.append(n[:mid_i_floor-1] + 2 * mid_char + n[mid_i_ceil+1:])
            else:
                candidates.append(n[:mid_i_floor] + mid_char + n[mid_i_ceil:])
        leng = len(n)
        candidates += ['9' * leng, '9' * (leng-1)]
        candidates += ['1'+'0'*(leng-2)+'1', '1'+'0'*(leng-1)+'1']
        candidates = [can for can in candidates if can and can != n]
        return min(candidates, key=lambda x: (abs(int(n) - int(x)), int(x)))


if __name__ == '__main__':
    sol = Solution()
    print(sol.nearestPalindromic("1"), '0')
    print(sol.nearestPalindromic("0"), '1')
    print(sol.nearestPalindromic("1231"), '1221')
    print(sol.nearestPalindromic("1221"), '1111')
    print(sol.nearestPalindromic("1000"), '999')
    print(sol.nearestPalindromic("999"), '1001')
    print(sol.nearestPalindromic("1283"), '1331')
    print(sol.nearestPalindromic("12389"), '12421')

    print(sol.nearestPalindromic("121"), '111')  # change middle
    print(sol.nearestPalindromic("123456"), '123321')  # change tail