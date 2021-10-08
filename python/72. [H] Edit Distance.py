class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        dp = [i for i in range(len1 + 1)]
        for c2 in word2:
            upper_left = dp[0]
            dp[0] += 1
            for i, c1 in enumerate(word1, 1):
                next_upper_left = dp[i]
                dp[i] = min(dp[i-1], dp[i], upper_left) + 1
                if c1 == c2:
                    dp[i] = min(dp[i], upper_left)
                upper_left = next_upper_left
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance('abc', 'bcd'))
