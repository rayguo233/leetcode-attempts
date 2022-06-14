from typing import List


class UF:

    def __init__(self) -> None:
        self.parent = {}

    def add(self, child):
        self.parent[child] = child

    def union(self, parent, child):
        if parent not in self.parent or child not in self.parent:
            return
        parent = self.find(parent)
        self.parent[child] = parent

    def find(self, child) -> int:
        if self.parent[child] != child:
            parent = self.find(self.parent[child])
            self.parent[child] = parent
        return self.parent[child]


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UF()
        for num in nums:
            uf.add(num)
            uf.union(num - 1, num)
            uf.union(num, num + 1)
        res = 0
        for num in nums:
            parent = uf.find(num)
            res = max(res, num - parent + 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
