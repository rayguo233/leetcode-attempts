from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        sets = [set(), set()]  # type: List[Set[int]]
        return all(self.dfs(u, 0, graph, sets) for u in range(len(graph)) if u not in sets[0] and u not in sets[1])

    def dfs(self, u, set_i, graph, sets) -> bool:
        this_set, other_set = sets[set_i], sets[not set_i]
        if u in this_set:
            return True
        if u in other_set:
            return False
        this_set.add(u)
        return all(self.dfs(v, not set_i, graph, sets) for v in graph[u])

if __name__ == '__main__':
    sol = Solution()
    print(sol.isBipartite([[1], [0]]))
