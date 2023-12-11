class Solution:

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (k + maxPts)
        prev_sum = 0
        for i in range(1, k + maxPts):
            begin_i = max(1, i - maxPts)
            prev_sum -= dp[begin_i - 1]
            dp[i] = prev_sum + int(i <= maxPts)
            if i < k:
                prev_sum += dp[i]
        numerator, denominator = 0, 0.
        # print(dp)
        for i in range(k, k + maxPts):
            denominator += dp[i]
            if i <= n:
                numerator += dp[i]
        return numerator / denominator


if __name__ == '__main__':
    sol = Solution()
    print(sol.new21Game(6, 1, 10))