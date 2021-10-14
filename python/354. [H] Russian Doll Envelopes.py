from collections import OrderedDict
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
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
    # assert(sol.rob([2,1,4]) == 4)
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
