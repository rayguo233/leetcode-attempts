import bisect
import collections
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = [i for i, to_nodes in enumerate(graph) if not to_nodes]
        stack = safe_nodes.copy()
        graph = [set(g) for g in graph]
        while stack:
            safe_node = stack.pop()
            for i, s in enumerate(graph):
                if safe_node in s:
                    s.remove(safe_node)
                    if not s:
                        safe_nodes.append(i)
                        stack.append(i)
        return sorted(safe_nodes)




if __name__ == '__main__':
    sol = Solution()
    print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
    print(sol.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
