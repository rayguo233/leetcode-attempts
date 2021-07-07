# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        d = defaultdict(int)
        min_len = 0

        while right < len(s):
            c = s[right]
            right += 1
            # if `c` is unique in the window
            if d[c] == 0:
                d[c] = 1
                # if new solution found
                if right - left > min_len:
                    min_len = right - left
            # if `c` is a duplicate in the window
            else:
                # shrink window until another `c` encountered
                while s[left] != c:
                    d[s[left]] -= 1
                    left += 1
                d[c] = 1
                left += 1

        return min_len





if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('sdffssdfgghjk'))
    print(sol.lengthOfLongestSubstring('sdfsdfs'))
    print(sol.lengthOfLongestSubstring(''))
