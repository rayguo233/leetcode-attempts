# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# You are given an array prices where prices[i] is the price of a
# given stock on the ith day, and an integer fee representing a
# transaction fee.
#
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like, but you need to pay the transaction fee for
# each transaction.
#
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
#
# 1 <= prices.length
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        dp_hold, dp_sold = - prices[0], 0
        for p in prices[1:]:
            dp_hold, dp_sold = max(dp_hold, dp_sold - p), max(dp_sold, dp_hold + p - fee)
        return max(dp_sold, 0)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([2,1,4], 2))
    print(sol.maxProfit([2,1,4], 2))
