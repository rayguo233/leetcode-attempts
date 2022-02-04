import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        p2p = [-1] * n
        for x, y in pairs:
            p2p[x], p2p[y] = y, x
        p2pref = [set()] * n  # type: List[set[int]]
        for p, pref in enumerate(preferences):
            p2pref[p] = set(pref[:pref.index(p2p[p])])
        print(p2pref)
        cheater = set()
        for p in range(n):
            for other in p2pref[p]:
                if p in p2pref[other]:
                    cheater.add(other)
                    cheater.add(p)
        return len(cheater)

if __name__ == '__main__':
    sol = Solution()
    print(sol.unhappyFriends(6,
[[1,4,3,2,5],[0,5,4,3,2],[3,0,1,5,4],[2,1,4,0,5],[2,1,0,3,5],[3,4,2,0,1]],
[[3,1],[2,0],[5,4]]))