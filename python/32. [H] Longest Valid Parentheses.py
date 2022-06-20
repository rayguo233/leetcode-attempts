from typing import List, Optional


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        stack = []
        i_to_prev_i = [i for i in range(len(s))]
        longest = 0
        for i, c in enumerate(s):
            if c == ')':
                if not stack:
                    continue
                prev_i = stack.pop()
                if prev_i > 0 and i_to_prev_i[prev_i - 1] != prev_i - 1:
                    i_to_prev_i[i] = i_to_prev_i[prev_i - 1]
                else:
                    i_to_prev_i[i] = prev_i
                longest = max(longest, i - i_to_prev_i[i] + 1)
            else:
                stack.append(i)
        return longest


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses('())()())'))
    print(sol.longestValidParentheses('(()'))
    print(sol.longestValidParentheses('(()()'))
