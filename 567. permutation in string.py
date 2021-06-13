# https://leetcode-cn.com/problems/permutation-in-string/

# Given two strings s1 and s2, return true if s2 contains the permutation of s1.
#
# In other words, one of s1's permutations is the substring of s2.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutation-in-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left2 = right2 = 0
        leng1, leng2 = len(s1), len(s2)
        d1, d2 = defaultdict(int), defaultdict(int)
        cur_matched = 0  # number of chars that has already been matched

        # build dict of s1
        for c in s1: d1[c] += 1

        while right2 < leng2:
            # if match found
            if cur_matched == leng1:
                return True

            # expand window
            char = s2[right2]
            right2 += 1

            print(d1, d2, char, left2)

            # if `char` not in `s1`
            if char not in d1:
                cur_matched = 0
                d2 = defaultdict(int)
                left2 = right2
            # elif `char` in `s1` and not in excess
            elif d2[char] < d1[char]:
                d2[char] += 1
                cur_matched += 1
            # else `char` in `s1` and is in excess
            else:
                # shrink window
                while left2 < right2 and d2[s2[left2]] > 0:
                    if s2[left2] == char:
                        left2 += 1
                        break
                    else:
                        d2[s2[left2]] -= 1
                        cur_matched -= 1
                        left2 += 1


        return cur_matched == leng1



if __name__ == '__main__':
    sol = Solution()
    # print(sol.checkInclusion("ADO", 'ADDDDDAO'))
    # print(sol.checkInclusion("ADOR", 'ADDDDDAO'))
    print(sol.checkInclusion("adtc", 'tdcdat'))