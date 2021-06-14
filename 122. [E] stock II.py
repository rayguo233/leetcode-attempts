# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

# You are given an array prices where prices[i] is the price
# of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete as
# many transactions as you like (i.e., buy one and sell one share
# of the stock multiple times).
#
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp_hold, dp_sold = - prices[0], 0
        for price in prices[1:]:
            dp_hold, dp_sold = max(dp_hold, dp_sold - price), max(dp_sold, dp_hold + price)
        return dp_sold





if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1,2,3,2,5]))
