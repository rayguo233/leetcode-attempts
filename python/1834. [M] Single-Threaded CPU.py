import bisect
import heapq
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((eqtime, pctime, i) for i, (eqtime, pctime) in enumerate(tasks))
        curr_time = 0
        ans = []
        hq = []
        i = 0
        while i < len(tasks):
            eqtime, pctime, prev_i = tasks[i]
            if curr_time >= eqtime:
                heapq.heappush(hq, (pctime, prev_i))
                i += 1
                continue
            if not hq:
                heapq.heappush(hq, (pctime, prev_i))
                curr_time = eqtime
                i += 1
                continue
            while curr_time < eqtime and hq:
                task_pctime, task_i = heapq.heappop(hq)
                ans.append(task_i)
                curr_time += task_pctime
        while hq:
            ans.append(heapq.heappop(hq)[1])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.getOrder([[1,2],[2,4],[3,2],[4,1]]), [0,2,3,1])
    print(sol.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]), [0,2,3,1])
