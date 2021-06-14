# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

# You are given an integer array prices where prices[i] is
# the price of a given stock on the ith day, and an integer k.
#
# Find the maximum profit you can achieve. You may complete
# at most k transactions.
#
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
#
# 0 <= k <= 100
# 0 <= prices.length
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        dp_hold, dp_sold = [- float('inf')] * (k+1), [- float('inf')] * (k+1)
        dp_sold[0] = 0
        for p in prices:
            # print(dp_hold, dp_sold, p)
            for i in range(1, k + 1):
                dp_hold[i], dp_sold[i] = max(dp_hold[i], dp_sold[i-1] - p), \
                                         max(dp_sold[i], dp_hold[i] + p)
        return int(max(dp_sold + [0]))





if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(2, [3,2,6,5,0,3]))
