# https://leetcode-cn.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return
# the minimum window substring of s such that every character in t
# (including duplicates) is included in the window. If there is
# no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-window-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''

        min_str = ""
        cur_match, target_match = 0, len(t)
        in_window, target = defaultdict(int), defaultdict(int)
        left, right = 0, 0  # [left, right)
        leng = len(s)

        # initialize target
        for c in t:
            target[c] += 1

        while right < leng or cur_match == target_match:
            # print(s[left:right], cur_match, target_match)
            # expand window
            if cur_match != target_match:
                char = s[right]
                right += 1
                if char not in target: continue
                in_window[char] += 1
                if in_window[char] <= target[char]:
                    cur_match += 1

            # shrink window
            if cur_match == target_match:
                # if it's the new answer
                if min_str == "" or right - left < len(min_str):
                    min_str = s[left:right]

                # shrink window by 1
                char = s[left]
                left += 1
                if char not in target: continue
                in_window[char] -= 1
                if in_window[char] + 1 <= target[char]:
                    cur_match -= 1

        return min_str

    def minWindow_clean(self, s: str, t: str) -> str:
        left, right = 0, 0  # [left, right)
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        num_valid = 0  # type: int
        min_start, min_len = 0, float('inf')
        for c in t: dict_t[c] += 1

        while right < len(s):
            c = s[right]
            right += 1

            if c not in dict_t: continue
            # print(dict_s, c, num_valid, len(dict_t))

            dict_s[c] += 1

            if dict_s[c] < dict_t[c]:
                continue
            else:
                if dict_s[c] == dict_t[c]: num_valid += 1
                if num_valid == len(dict_t):
                    # print('shrink', dict_s)
                    # shrink window
                    while True:
                        remove = s[left]
                        if remove in dict_t and dict_s[remove] == dict_t[remove]:
                            break
                        left += 1
                        if remove in dict_t and dict_s[remove] > dict_t[remove]:
                            dict_s[remove] -= 1
                    # record new result
                    if right - left < min_len:
                        min_start, min_len = left, right - left

        return '' if min_len == float('inf') else s[ min_start : (min_start + min_len) ]





if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
    print(sol.minWindow_clean("a", 'aa'))
    # print(sol.minWindow_clean("ASDF", ''))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
