import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = '01'
        row_len = 2 ** (n - 1)
        while k > 2:
            row_len //= 2
            if k > row_len:
                k -= row_len
                curr = curr[1]
            else:
                curr = curr[0]
            curr = '01' if curr == '0' else '10'
        return int(curr[k-1])



if __name__ == '__main__':
    sol = Solution()
    print(sol.kthGrammar(1, 1), 0)
    print(sol.kthGrammar(2, 1), 1)
    print(sol.kthGrammar(3, 3), 1)
    print(sol.kthGrammar(4, 3), 1)

