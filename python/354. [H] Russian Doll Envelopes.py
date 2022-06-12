import bisect
from collections import OrderedDict
from typing import List


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        envelopes = [e[1] for e in envelopes]
        max_len = 0
        for i, h in enumerate(envelopes):
            envelopes[i] = float('inf')
            index = bisect.bisect_left(envelopes, h, hi=max_len)
            envelopes[index] = min(h, envelopes[index])
            max_len = max(index + 1, max_len)
        return max_len

    def maxEnvelopes_v0(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        d = OrderedDict()
        d[0] = [[0, 0]]
        max_env = 0
        for env in envelopes:
            depth = 0
            for key, vals in reversed(d.items()):
                for val in vals:
                    if val[0] < env[0] and val[1] < env[1]:
                        depth = key + 1
                        break
                if depth:
                    break
            if depth not in d:
                d[depth] = [env]
            else:
                d[depth].append(env)
            max_env = max(depth, max_env)
        return max_env


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxEnvelopes([[1, 3], [4, 2]]))
    print(sol.maxEnvelopes([[1, 3], [4, 4]]))
