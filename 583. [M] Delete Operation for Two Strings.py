# https://leetcode.com/problems/delete-operation-for-two-strings/

# Given two strings word1 and word2, return the minimum
# number of steps required to make word1 and word2 the same.
#
# In one step, you can delete exactly one character in either string.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        short, long = word1, word2
        if len(word1) > len(word2):
            short, long = word2, word1

        dp = [0] * (len(short) + 1)
        diag = 0
        for i in range(len(long) + 1):
            for j in range(len(short) + 1):
                next_diag = dp[j]
                if i == 0 or j == 0:
                    dp[j] = i + j
                elif long[i-1] == short[j-1]:
                    dp[j] = diag
                else:
                    dp[j] = min(dp[j], dp[j-1]) + 1
                diag = next_diag
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance('sea', 'eat'))
