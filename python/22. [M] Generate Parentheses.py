from functools import lru_cache
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @lru_cache(None)
        def generate_with_l_left_r_right(l: int, r: int) -> List[str]:
            if l == r == 0:
                return ['']
            if l < 0 or r < 0:
                return []
            res = []
            res += ['(' + sub_res for sub_res in generate_with_l_left_r_right(l-1, r)]
            if r > l:
                res += [')' + sub_res for sub_res in generate_with_l_left_r_right(l, r-1)]
            return res

        return generate_with_l_left_r_right(n, n)

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(4))
