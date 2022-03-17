import collections
import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        hq = []
        day_rotten_to_num = collections.defaultdict(int)
        total_eaten = 0
        for i, day in enumerate(days):
            apple = apples[i]
            if apple:
                day_rotten = i + day
                day_rotten_to_num[day_rotten] += apple
                heapq.heappush(hq, day_rotten)
            while hq and hq[0] <= i:
                heapq.heappop(hq)
            if not hq:
                continue 
            total_eaten += 1
            day_rotten_to_num[hq[0]] -= 1
            if day_rotten_to_num[hq[0]] == 0:
                heapq.heappop(hq)
        i += 1
        while hq:
            if hq[0] <= i:
                heapq.heappop(hq)
            else:
                total_eaten += 1
                day_rotten_to_num[hq[0]] -= 1
                if day_rotten_to_num[hq[0]] == 0:
                    heapq.heappop(hq)
                i += 1
        return total_eaten


if __name__ == '__main__':
    s = Solution()
    print(s.eatenApples([0,1],[0,1]))
    print(s.eatenApples([0,2],[0,2]))
    print(s.eatenApples([0,3],[0,3]))
    print(s.eatenApples([2,0],[1,0]))
    print(s.eatenApples([2,0],[1,0]))