import math
from typing import List


class Solution:

    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        n = int(math.sqrt(finalSum))
        while ((1 + n) * n) > finalSum:
            n -= 1
        res = [2 * i for i in range(1, n + 1)]
        res[-1] += finalSum - ((1 + n) * n)
        return res

    def maximumEvenSplit_version0(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        final_sum = finalSum / 2
        i = 1
        res = []
        while final_sum - i >= 0:
            final_sum -= i
            res.append(i * 2)
            i += 1
        res[-1] += int(final_sum * 2)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumEvenSplit(6))
    print(sol.maximumEvenSplit(8))
    print(sol.maximumEvenSplit(28))