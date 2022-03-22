import sys
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        curr_heater_i = 0
        houses.sort()
        heaters.sort()
        heaters = [-3 * (10 ** 9)] + heaters + [sys.maxsize]
        min_radius = 0
        for house in houses:
            while heaters[curr_heater_i+1] <= house:
                curr_heater_i += 1
                continue
            min_radius = max(min_radius,
                             min(house - heaters[curr_heater_i],
                                 heaters[curr_heater_i+1] - house)
                            )
            print(house, heaters[curr_heater_i], min_radius)
        return min_radius



if __name__ == '__main__':
    sol = Solution()
    print(sol.findRadius([1], [2,3]), 1)
    print(sol.findRadius([1], [10 ** 9]), 10 ** 9 - 1)
    print(sol.findRadius([1], [10 ** 9, 10]), 9)
    print(sol.findRadius([10], [1,5]), 5)
    print(sol.findRadius([2,10], [1]), 9)
    print(sol.findRadius([2,10], [5]), 5)
    print(sol.findRadius([2,10], [11]), 11 - 2)
