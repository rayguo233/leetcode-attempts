# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# You are given an array prices where prices[i] is the price of a
# given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the
# stock multiple times) with the following restrictions:
#
# After you sell your stock, you cannot buy stock on the next day
# (i.e., cooldown one day).
#
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp_hold, dp_sold = [- float('inf')] * 2, [0] * 2
        cur_index = 0
        dp_sold[cur_index] = 0
        for p in prices:
            dp_hold[cur_index], dp_sold[cur_index] = max(dp_hold[not cur_index], dp_sold[cur_index] - p), \
                                                     max(dp_sold[not cur_index], dp_hold[not cur_index] + p)
            cur_index = not cur_index
        return int(max(dp_sold + [0]))

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([2,1,4]))
    assert(sol.maxProfit([1,2,1,2]) == 1)
