from typing import Tuple

LEFT, RIGHT = 0, 1

class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = ''
        i = 0
        rvsd = False
        while True:
            while i < len(s) and s[i] != '(':
                res += s[i]
                i += 1
            if i == len(s):
                return res
            add_res, i = self.get_bracketed_str(s, i + 1)
            res += add_res

    def get_bracketed_str(self, s: str, start: int) -> Tuple[str, int]:
        res = ''
        i = start
        while True:
            while s[i] not in '()':
                res += s[i]
                i += 1
            if s[i] == '(':
                add_res, i = self.get_bracketed_str(s, i+1)
                res += add_res
            else:
                break
        # print(res, '---')
        return res[::-1], i + 1



if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseParentheses("ta()usw((((a))))"), 's')
    print(sol.reverseParentheses('s'), 's')
    print(sol.reverseParentheses('(s)'), 's')
    print(sol.reverseParentheses('(asd)'), 'dsa')
    print(sol.reverseParentheses('(asd(hgf)jkl)'), 'lkjhgfdsa')
    print(sol.reverseParentheses('(asd(h(gf))jkl)'), 'lkjhfgdsa')
    print(sol.reverseParentheses('(asd(h(gf)asb)jkl)'), 'lkjhfgasbdsa')

    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
