import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def racecar(self, target: int) -> int:
        pos, speed = 0, 1
        steps = 1
        while pos + speed < target:
            steps += 1
            pos += speed
            speed *= 2
        if pos + speed == target:
            return steps
        return steps + 1 + min(self.racecar(target - pos), self.racecar(pos + speed - target))


if __name__ == '__main__':
    sol = Solution()
    print(sol.racecar(1), 1)
    print(sol.racecar(2), 4)
    print(sol.racecar(3), 2)
    print(sol.racecar(6))
