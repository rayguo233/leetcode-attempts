import collections
from typing import List


class DetectSquares:

    def __init__(self):
        self.p_to_freq = collections.defaultdict(int)
        self.x_to_p = collections.defaultdict(list)
        # self.y_to_p = collections.defaultdict(list)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.p_to_freq[point] += 1
        self.x_to_p[point[0]].append(point)
        # self.y_to_p[point[1]].append(point)

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        res = 0
        for _, y1 in self.x_to_p[x0]:
            side_len = abs(y0 - y1)
            for delta_x in [side_len, -side_len]:
                x2, y2 = x0 + delta_x, y0
                x3, y3 = x0 + delta_x, y1
                res += self.p_to_freq[(x2, y2)] * self.p_to_freq[(x3, y3)]
        return res


if __name__ == '__main__':
    pass