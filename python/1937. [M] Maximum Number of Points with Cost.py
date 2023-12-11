from typing import List


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        num_cols = len(points[0])
        prev_dp = points[0].copy()
        curr_dp = [0] * num_cols
        for row in points[1:]:
            for curr_col, curr_cell in enumerate(row):
                for prev_col, prev_cell in enumerate(prev_dp):
                    new_val = prev_cell + curr_cell - abs(curr_col - prev_col)
                    curr_dp[curr_col] = max(curr_dp[curr_col], new_val)
            prev_dp = curr_dp
            curr_dp = [0] * num_cols
        return max(prev_dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters('abaacbbca'))
    print(sol.removeDuplicateLetters('abadddacbddbc'))