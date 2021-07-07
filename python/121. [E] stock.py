# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price
# of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day
# to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
#
# 1 <= prices.length
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp_hold, dp_sold = - prices[0], 0
        for price in prices[1:]:
            dp_hold, dp_sold = max(dp_hold, - price), max(dp_sold, dp_hold + price)
        return dp_sold





if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1,2,3,2]))
