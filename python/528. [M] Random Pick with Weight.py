import bisect
from random import randint
from typing import List


class Solution:
    max_rand_num: int
    rand_nums: List[int]

    def __init__(self, weights: List[int]):
        self.rand_nums = []
        curr_rand_num = 0
        for w in weights:
            curr_rand_num += w
            self.rand_nums.append(curr_rand_num)
        self.max_rand_num = self.rand_nums[-1]

    def pickIndex(self) -> int:
        rand_num = randint(1, self.max_rand_num)
        return bisect.bisect_left(self.rand_nums, rand_num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

if __name__ == '__main__':
    pass
