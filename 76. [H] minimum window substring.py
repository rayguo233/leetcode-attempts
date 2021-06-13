# https://leetcode-cn.com/problems/minimum-window-substring/

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

if __name__ == '__main__':
    sol = Solution()
    assert(sol.minWindow("ADOBECODEBANC", 'ABC') == 'BANC')
    assert(sol.minWindow("", 'ABC') == '')
    assert(sol.minWindow("", '') == '')
    assert(sol.minWindow("ASDF", '') == '')
    print(sol.minWindow("ADOBECODEBANC", 'ABC'))
    print(sol.minWindow("ADOBECODEBANC", 'ABC'))
