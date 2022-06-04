class Solution:

    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int,
                       targetSeconds: int) -> int:
        num_min = targetSeconds // 60
        num_sec = targetSeconds % 60
        cost = float('inf')
        if num_min <= 99:
            cost = self.get_cost(num_min, num_sec, moveCost, pushCost, startAt)
        if num_sec + 60 <= 99:
            cost = min(
                cost,
                self.get_cost(num_min - 1, num_sec + 60, moveCost, pushCost,
                              startAt))
        return int(cost)

    def get_cost(self, num_min: int, num_sec: int, move_cost, push_cost,
                 start_at) -> int:
        start_at = str(start_at)
        str_min = str(num_min)
        str_sec = str(num_sec)
        if len(str_sec) == 1 and str_min != '0':
            str_sec = '0' + str_sec
        str_target = str_min + str_sec
        if str_min == '0':
            str_target = str_sec
        cost = 0
        for char in str_target:
            if char != start_at:
                cost += move_cost
                start_at = char
            cost += push_cost
        return cost


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostSetTime(1, 2, 1, 600))
    print(sol.minCostSetTime(0, 1, 2, 76))