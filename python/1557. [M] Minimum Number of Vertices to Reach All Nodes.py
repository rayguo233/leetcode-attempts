import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(n)]
        def union(p: List[int], child: int) -> int:
            if p[child] == child:
                return child
            p[child] = union(p, p[child])
            return p[child]
        for f, t in edges:
            parent[t] = union(parent,f)
        for child, prnt in enumerate(parent):
            parent[child] = union(parent, parent[child])
        return list(set(parent))


if __name__ == '__main__':
    sol = Solution()
    print(sol.racecar(1), 1)
    print(sol.racecar(2), 4)
    print(sol.racecar(3), 2)
    print(sol.racecar(6))
