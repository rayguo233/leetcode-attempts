from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.curr_num = 0        
        self.max_curr_num = len(encoding) - 2

    def next(self, n: int) -> int:
        while self.curr_num <= self.max_curr_num:
            if self.encoding[self.curr_num] >= n:
                self.encoding[self.curr_num] -= n
                return self.encoding[self.curr_num + 1]
            n -= self.encoding[self.curr_num]
            self.curr_num += 2
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)


if __name__ == '__main__':
