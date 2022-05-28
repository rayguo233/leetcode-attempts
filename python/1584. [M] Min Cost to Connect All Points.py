import heapq
from typing import List


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hp = []
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i + 1:], i + 1):
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(hp, (dist, i, j))
        print(hp)
        res = 0
        uf = Union(len(points))
        for _ in range(len(points) - 1):
            i, j = 0, 0
            while uf.find(i) == uf.find(j):
                dist, i, j = heapq.heappop(hp)
            # print(dist, f'{points[i]} - {points[j]}', i, uf.find(i), j,
            #   uf.find(j))
            res += dist
            uf.union(j, i)

        return res


class Union:

    def __init__(self, size: int) -> None:
        self.p = [i for i in range(size)]

    def find(self, c: int) -> int:
        if self.p[c] != self.p[self.p[c]]:
            self.p[c] = self.find(self.p[c])
        return self.p[c]

    def union(self, c: int, p: int) -> None:
        self.p[self.find(c)] = self.find(p)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print(sol.minCostConnectPoints([[1, 2], [-15, 19], [-18, -15], [-7, 14]]))
