# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

# You are given an array prices where prices[i] is the
# price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete
# at most two transactions.
#
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp_hold1, dp_sold1 = - prices[0], - float('inf')
        dp_hold2, dp_sold2 = - float('inf'), - float('inf')
        for price in prices[1:]:
            dp_hold2, dp_sold2 = max(dp_hold2, dp_sold1 - price), max(dp_sold2, dp_hold2 + price)
            dp_hold1, dp_sold1 = max(dp_hold1, - price), max(dp_sold1, dp_hold1 + price)
        return max(0, dp_sold1, dp_sold2)





if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1,2,3,2,5,2,4]))
