import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        stop_to_route = defaultdict(list)  # type: Dict[int, List[int]]
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].append(i)
        dq = deque([source])
        visited = {source}
        steps = 0
        while dq:
            steps += 1
            for _ in range(len(dq)):
                stop = dq.popleft()
                for route_i in stop_to_route[stop]:
                    for next_stop in routes[route_i]:
                        if next_stop in visited:
                            continue
                        if next_stop == target:
                            return steps
                        dq.append(next_stop)
                        visited.add(next_stop)
                    routes[route_i] = []

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
    print(sol.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12))
