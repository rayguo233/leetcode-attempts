from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        node_to_neighbors = [set() for _ in range(n)]
        for a, b in edges:
            node_to_neighbors[a].add(b)
            node_to_neighbors[b].add(a)
        node_to_height = [0] * n 

        def dfs(node: int, depth: int) -> int:
            neighbor_heights = [(0, -1), (0, -1)]
            for next_node in node_to_neighbors[node]:
                node_to_neighbors[next_node].remove(node)
                next_node_height = dfs(next_node, depth+1)
                neighbor_heights.append((next_node_height, next_node))
            neighbor_heights = sorted(neighbor_heights)[-2:]
            max_height = neighbor_heights[-1][0] + 1
            neighbor_heights = sorted(neighbor_heights + [(depth - 1, node)])
            for next_node in node_to_neighbors[node]:
                if next_node != neighbor_heights[-1][1]:
                    node_to_height[next_node] = neighbor_heights[-1][0] + 2
                else:
                    node_to_height[next_node] = max(neighbor_heights[-1][0],
                                                    neighbor_heights[-2][0] + 2)
            print(node, depth, max_height, node_to_height, neighbor_heights)
            return max_height 
        
        node_to_height[0] = dfs(0, 1)
        min_height = min(node_to_height)
        return [node for node, height in enumerate(node_to_height) if height == min_height]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinHeightTrees(n = 5, edges = [[0,1],[0,2],[0,3],[3,4]]))
    print(sol.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
    print(sol.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))
    pass