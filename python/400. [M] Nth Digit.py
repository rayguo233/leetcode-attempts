import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def findNthDigit(self, n: int) -> int:
        num_digit = 1
        subtotal_digit = (10 ** num_digit - 10 ** (num_digit - 1)) * num_digit
        while n > subtotal_digit:
            n -= subtotal_digit
            num_digit += 1
            subtotal_digit = (10 ** num_digit - 10 ** (num_digit - 1)) * num_digit
        num = 10 ** (num_digit - 1) + (n // num_digit)
        if n % num_digit == 0:
            return int(str(num - 1)[-1])
        return int(str(num)[(n % num_digit) - 1])



if __name__ == '__main__':
    sol = Solution()
    print(sol.findNthDigit(1), 1)
    print(sol.findNthDigit(11), 0)
    print(sol.findNthDigit(12), 1)
