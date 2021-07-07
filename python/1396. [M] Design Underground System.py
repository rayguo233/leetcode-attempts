# https://leetcode.com/problems/design-underground-system/

from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.time = dict()
        self.ppl = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ppl[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.ppl[id]
        del self.ppl[id]
        key = startStation + '-' + stationName
        if key not in self.time:
            self.time[key] = [t - startTime, 1.]
        else:
            self.time[key][0] += t - startTime
            self.time[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + '-' + endStation
        return self.time[key][0] / self.time[key][1]

if __name__ == '__main__':
    pass
    # sol = Solution()
    # assert(sol.rob([0]) == 0)
    # assert(sol.rob([2,1,4]) == 6)
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 10)
    # assert(sol.rob([2,1,4,8,9]) == 15)
