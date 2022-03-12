import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
                continue
            if l == r or score == 0:
                return score
            power += tokens[r] - tokens[l]
            r -= 1
            l += 1
        return score

if __name__ == '__main__':
    sol = Solution()
    print(sol.bagOfTokensScore([1,30], 1))
    print(sol.bagOfTokensScore([2,30], 1))
    print(sol.bagOfTokensScore([1,1], 1))
    print(sol.bagOfTokensScore([1,1,1,3], 1))
