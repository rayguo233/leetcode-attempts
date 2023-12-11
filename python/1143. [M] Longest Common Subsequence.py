from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0] * len2 for _ in range(len1)]

        def get(r, c) -> int:
            if r < 0 or c < 0:
                return 0
            return dp[r][c]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                dp[i][j] = max(get(i-1, j-1) + (c1 == c2), get(i-1, j), get(i, j-1))
        return dp[len1-1][len2-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonSubsequence('s', 's'))
    print(sol.longestCommonSubsequence('b', 'a'))
    print(sol.longestCommonSubsequence('aba', 'baa'))
