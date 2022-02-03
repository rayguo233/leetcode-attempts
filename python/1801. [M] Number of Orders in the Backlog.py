import bisect
import heapq
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


BUY, SELL = 0, 1
PRICE, AMT = 0, 1

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        bklogs = [[], []]
        for price, amt, type in orders:
            while amt and bklogs[not type] and \
                    ((type == BUY and bklogs[SELL][0][PRICE] <= price) or
                     (type == SELL and - bklogs[BUY][0][PRICE] >= price)):
                amt_have = bklogs[not type][0][AMT]
                if amt < amt_have:
                    bklogs[not type][0][AMT] -= amt
                    amt = 0
                else:
                    amt -= bklogs[not type][0][AMT]
                    heapq.heappop(bklogs[not type])
            if amt:
                heapq.heappush(bklogs[type], [price * (-1 if type == BUY else 1), amt])
            # print(bklogs)
        res = 0
        for bklog in bklogs:
            for price, amt in bklog:
                res += amt
        return res % (10 ** 9 + 7)



if __name__ == '__main__':
    sol = Solution()
    print(sol.getNumberOfBacklogOrders(orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]), 6)
    print(sol.getNumberOfBacklogOrders(orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]), 999999984)
