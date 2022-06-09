import collections
import heapq
from typing import List


class Solution:

    def maxProbability(self, n: int, edges: List[List[int]],
                       succProb: List[float], start: int, end: int) -> float:
        node_to_neighbors = collections.defaultdict(list)
        node_to_prob = collections.defaultdict(float)
        nodes_visited = set()
        heap = [(-1., start)]
        node_to_prob[start] = 1.
        for i, (a, b) in enumerate(edges):
            node_to_neighbors[a].append((b, i))
            node_to_neighbors[b].append((a, i))
        print(node_to_neighbors)
        while heap:
            print(heap)
            curr_prob, from_node = heapq.heappop(heap)
            curr_prob = -curr_prob
            for next_node, edge in node_to_neighbors[from_node]:
                if next_node in nodes_visited:
                    continue
                next_node_new_prob = curr_prob * succProb[edge]
                if next_node_new_prob <= node_to_prob[next_node]:
                    continue
                heapq.heappush(heap, (-next_node_new_prob, next_node))
                node_to_prob[next_node] = next_node_new_prob
            nodes_visited.add(from_node)
        return node_to_prob[end]


if __name__ == '__main__':
    sol = Solution()
    print(
        sol.maxProbability(n=3,
                           edges=[[0, 1], [1, 2], [0, 2]],
                           succProb=[0.5, 0.5, 0.2],
                           start=0,
                           end=2))
