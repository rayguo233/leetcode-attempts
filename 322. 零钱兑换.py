# https://leetcode-cn.com/problems/coin-change/

# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可
# 以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回-1。
#
# 你可以认为每种硬币的数量是无限的。

INF = float('inf')

class Solution:
    @staticmethod
    def coin_change_failed(coins: list[int], amount: int) -> int:
        max_coin = max(coins)
        dp = [float('inf')] * max_coin
        dp[0] = 0

        def get_prev(amt, coin_val):
            index = (amt - coin_val) % max_coin
            return float('inf') if index < 0 else dp[index]

        for val in range(1, amount + 1):
            minimum = float('inf')
            for coin in coins:
                minimum = min(minimum, 1 + get_prev(val, coin))
            ind = val % max_coin
            dp[ind] = min(minimum, float('inf'))

        res = dp[amount % max_coin]
        return -1 if res == INF else res

    @staticmethod
    def coin_change(coins: list[int], amount: int) -> int:
        record = {}

        return record

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    print(sol.coin_change([1,2,5], 11))
    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
