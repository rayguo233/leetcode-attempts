import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s) + 1
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n-i):
                if i == 0:
                    dp[i][j] = 1
                    continue
                if s[i-1] == 'D':
                    dp[i][j] = sum(dp[i-1][j+1:]) % (10 ** 9 + 7)
                else: # s[i-1] == 'I':
                    dp[i][j] = sum(dp[i-1][:j+1]) % (10 ** 9 + 7)
        return dp[n-1][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numPermsDISequence('D'))
    print(sol.numPermsDISequence('DID'))
