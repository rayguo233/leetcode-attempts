from copy import copy
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.dfs(graph, 0, [0])
        return self.res

    def dfs(self, graph, index, path_so_far: List[int]) -> None:
        target = len(graph) - 1
        if index == target:
            self.res.append(path_so_far)
            return
        for next_index in graph[index]:
            self.dfs(graph, next_index, copy(path_so_far) + [next_index])


if __name__ == '__main__':
    sol = Solution()
    print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
