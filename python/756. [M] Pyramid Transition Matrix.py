import collections
from typing import Dict, List, Tuple


class Solution:

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = collections.defaultdict(list)
        for l, r, t in allowed:
            d[(l, r)].append(t)
        return self.dfs(d, bottom, 0, '')

    def dfs(self, allowed: Dict[Tuple[str, str], List[str]], bottom: str,
            bott_i: int, top: str) -> bool:
        if bott_i == len(bottom) - 1:
            if bott_i == 0:
                return True
            return self.dfs(allowed, top, 0, '')
        for t in allowed[(bottom[bott_i], bottom[bott_i + 1])]:
            if self.dfs(allowed, bottom, bott_i + 1, top + t):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1, 1, 2]))
    print(sol.permuteUnique([1, 1, 2, 2]))
