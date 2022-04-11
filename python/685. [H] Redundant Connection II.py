from typing import List

class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = [i for i in range(size+1)]

    def union(self, parent: int, child: int) -> None:
        self.parent[child] = self.find(parent)

    def find(self, child: int) -> int:
        parent = self.parent[child]
        if parent != child:
            self.parent[child] = self.find(parent)
        return self.parent[child]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(size=n)
        candidates = []
        cand = None
        for parent, child in edges:
            if not candidates and uf.parent[child] != child:
                for p, c in edges:
                    if c == child:
                        other_parent = p
                        break
                candidates = [[parent, child], [other_parent, child]]
                continue
            if uf.find(parent) == child:
                cand = [parent, child]
            uf.union(parent, child)
        if not candidates:
            return cand
        uf.find(1)
        # print(uf.parent)
        if all(uf.find(parent) == uf.parent[1] for parent in uf.parent[1:]):
            return candidates[0]
        return candidates[1]