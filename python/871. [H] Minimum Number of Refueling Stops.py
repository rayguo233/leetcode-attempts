import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dq = deque([(0, startFuel)])
        num_refill = 0
        while dq:
            # print(dq)
            for _ in range(len(dq)):
                pos, fuel = deque.popleft(dq)
                if pos + fuel >= target:
                    return num_refill
                first_station = bisect.bisect_left(stations, [pos, float('inf')])
                # print(pos, fuel, first_station)
                for i in range(first_station, len(stations)):
                    sta_pos, sta_fuel = stations[i]
                    if pos + fuel < sta_pos:
                        break
                    new_fuel = fuel + sta_fuel + pos - sta_pos
                    if sta_pos + new_fuel >= target:
                        return num_refill + 1
                    dq.append((sta_pos, new_fuel))
            num_refill += 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.minRefuelStops(100, 50, [[25,30]]), -1)
    print(sol.minRefuelStops(1, 1, []))
    print(sol.minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))
    print(sol.minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))
    print(sol.minRefuelStops(target = 200, startFuel = 50, stations = [[25,25],[50,100],[100,100],[150,40]]))
