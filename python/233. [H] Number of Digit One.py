import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def countDigitOne(self, n: int) -> int:
        n = str(n)
        res = 0
        for i, digit in enumerate(reversed(n)):
            front = n[:-(i+1)]
            front = int(front) if front else 0
            res += (front + (digit > '1')) * (10 ** i)
            if digit == '1':
                back = int(n[-i:]) if i else 0
                res += back + 1
            # print(i, digit, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDigitOne(13), 6)
