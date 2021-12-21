from typing import Tuple


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        leng = len(s)
        next_i = 0
        total = 0
        while next_i < leng and s[next_i] == '(':
            next_sum, next_i = self.balance_par(s, next_i, leng)
            total += next_sum
        return total

    def balance_par(self, s: str, i: int, leng: int) -> Tuple[int, int]:
        if i == leng:
            return 0, i
        if s[i] == ')':
            return 1, i + 1
        if s[i:i+2] == '()':
            return 1, i + 2
        total = 0
        next_i = i + 1
        while next_i < leng and s[next_i] == '(':
            next_sum, next_i = self.balance_par(s, next_i, leng)
            total += next_sum
        return 2 * total, next_i + 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreOfParentheses('()'))
    print(sol.scoreOfParentheses('(())'))
    print(sol.scoreOfParentheses('(()()())'))
    print(sol.scoreOfParentheses('(())()()'))
    print(sol.scoreOfParentheses('((()()))'))
