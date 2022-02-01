from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:




if __name__ == '__main__':
    sol = Solution()
    print(sol.criticalConnections(2, [[0,1]]))
    print(sol.criticalConnections(3, [[0,1], [0,2], [1,2]]))
    print(sol.criticalConnections(4, [[0,1], [0,2], [1,2], [2,3]]))
    print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
