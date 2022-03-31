from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, temp in enumerate(reversed(temperatures)):
            i = n - i - 1
            while stack and stack[-1][1] <= temp:
                stack.pop()
            if stack:
                ans[i] = stack[-1][0] - i
            stack.append((i, temp))
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([1, 2, 3, 2, 4, 2, 1, 2, 1, 2, 6]))
