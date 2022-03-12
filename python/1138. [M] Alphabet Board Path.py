import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = ''
        start = 'a'
        for sub_target in target:
            res += self.func(start, sub_target)
            start = sub_target
        return res

    def func(self, start: str, end: str) -> str:
        x0, y0 = self.get_coord(start)
        x1, y1 = self.get_coord(end)
        x_dir = ('R' if x0 < x1 else 'L') * abs(x0 - x1)
        y_dir = ('D' if y0 < y1 else 'U') * abs(y0 - y1)
        print(x0, y0, x1, y1)
        return y_dir + x_dir + '!' if y0 == 5 else x_dir + y_dir + '!'

    def get_coord(self, letter: str) -> Tuple[int, int]:
        letter = ord(letter) - ord('a')
        y = letter // 5
        x = letter % 5
        return x, y

if __name__ == '__main__':
    sol = Solution()
    print(sol.alphabetBoardPath('zb'), -1)
