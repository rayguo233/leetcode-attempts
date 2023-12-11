from typing import List, Tuple


class UF:

    def __init__(self) -> None:
        pass

    def union(self, child, parent, factor):
        pass

    def find(self, child) -> Tuple[str, float]:
        pass


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        uf = UF()
        for (a, b), factor in zip(equations, values):
            if a > b:
                parent, child = b, a
            else:
                parent, child = a, b
                factor = 1 / factor
            uf.union(child, parent, factor)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
