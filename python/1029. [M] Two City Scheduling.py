from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -abs(x[1]-x[0]))
        n = int(len(costs) / 2)
        cities = [0, 0]
        total_cost = 0
        for cost in costs:
            min_i = cost[0] > cost[1]
            if cities[min_i] >= n:
                total_cost += cost[not min_i]
            else:
                cities[min_i] += 1
                total_cost += cost[min_i]
        return total_cost

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoCitySchedCost([[1,0],[10,20],[0,1],[100,98]]))
