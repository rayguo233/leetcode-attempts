# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses
# ( '(' or ')', in any positions ) so that the resulting
# parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and
# B are valid strings, or

# It can be written as (A), where A is a valid string.

from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        remove = []
        for i, c in enumerate(s):
            if c == '(':
                stack.appendleft(i)
            elif c == ')':
                if stack: stack.popleft()
                else: remove.append(i)
        remove += list(stack)
        remove.sort()
        res = ''
        start = 0
        if not remove: return s
        for i in remove:
            res += s[start:i]
            start = i + 1
        if remove[-1] < len(s) - 1:
            res += s[remove[-1]+1:]

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
