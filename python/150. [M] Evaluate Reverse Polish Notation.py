from curses.ascii import isdigit
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for tk in tokens:
            if any(isdigit(d) for d in tk):
                nums.append(int(tk))
                continue
            b, a = nums.pop(), nums.pop()
            if tk == '+':
                nums.append(a + b)
            elif tk == '-':
                nums.append(a - b)
            elif tk == '*':
                nums.append(a * b)
            elif tk == '/':
                nums.append(int(a / b))
        return nums[0]


if __name__ == '__main__':
    sol = Solution()
    # print(sol.evalRPN(['13', '5', '/']))
    # print(sol.evalRPN(["4", "13", "5", "/", "+"]))
    print(
        sol.evalRPN([
            "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
        ]))
