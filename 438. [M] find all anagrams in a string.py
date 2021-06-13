# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

# Given two strings s and p, return an array of all the start indices
# of p's anagrams in s. You may return the answer in any order.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s, p = p, s
        left, right = 0, 0  # [left, right)
        cur_matched = 0
        dict_s, dict_p = defaultdict(int), defaultdict(int)
        res = []
        len_s, len_p = len(s), len(p)

        # initialize dict_s
        for c in s: dict_s[c] += 1

        while right < len_p:
            print(dict_p, p[left])
            # if a match is found
            if cur_matched == len_s:
                res.append(left)

                # shrink window
                cur_matched -= 1
                dict_p[p[left]] -= 1
                left += 1

            # expand window
            char = p[right]
            right += 1
            # if char doesn't match anything in s
            if char not in dict_s:
                left = right
                cur_matched = 0
                dict_p = defaultdict(int)
            # if `char` matches something in `s` and is not in excess
            elif dict_p[char] < dict_s[char]:
                dict_p[char] += 1
                cur_matched += 1
            # if `char` matches something in `s` but is in excess
            else:
                # shrink window
                while left < right:
                    remove = p[left]
                    print('remove', remove)
                    left += 1
                    if remove == char: break
                    dict_p[remove] -= 1
                    cur_matched -= 1

        if cur_matched == len_s:
            res.append(left)

        return res





if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams('abcdcdcd', "cd"))
    print(sol.findAnagrams('cbaebabacd', "abc"))
