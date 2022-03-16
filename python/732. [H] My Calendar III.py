import bisect
from typing import List, Tuple

START, END, FREQ = 0, 1, 2

class MyCalendarThree:

    def __init__(self):
        self.events = []  # type: List[List[int, int, int]]   
        self.max_k = 1

    def book(self, start: int, end: int) -> int:
        res = self.insert_block(start, end, 1)
        print(start, end, res, self.events)
        return res

    def insert_block(self, start: int, end: int, freq):
        if start >= end: 
            return self.max_k
        i = bisect.bisect_left(self.events, [start, end, freq])
        if i - 1 >= 0 and self.events[i-1][END] >= end:
            #      ||||||
            # |||||||||||(|)
            i_1_end = self.events[i-1][END] 
            self.events[i-1][END] = start
            to_insert = [[start, end, self.events[i-1][FREQ] + 1]]
            self.max_k = max(self.max_k, to_insert[0][FREQ])
            self.events[i:i] = to_insert
            self.insert_block(end, i_1_end, self.events[i-1][FREQ])
            return self.max_k

        if i - 1 >= 0 and self.events[i-1][END] > start:
            # (|)|||||
            #  |||||
            i_1_end = self.events[i-1][END]
            if self.events[i-1][START] == start:
                self.events[i-1][FREQ] += 1
                self.max_k = max(self.events[i-1][FREQ], self.max_k)
            else:
                self.events[i-1][END] = start
                to_insert = [[start, i_1_end, self.events[i-1][FREQ] + 1]]
                self.max_k = max(self.max_k, to_insert[0][FREQ])
                self.events[i:i] = to_insert
            return self.insert_block(i_1_end, end, 1)

        if i < len(self.events) and self.events[i][START] == start:
            # |||(|)
            # |||||
            i_end = self.events[i][END]
            self.events[i][END] = end
            self.events[i][FREQ] += 1
            self.max_k = max(self.events[i][FREQ], self.max_k)
            return self.insert_block(end, i_end, self.events[i][FREQ] - 1)
        
        if i < len(self.events) and self.events[i][START] < end:
            # ||||||(||||)
            #    |||(|)
            i_end = self.events[i][END]
            self.events[i][FREQ] += 1
            self.events[i][END] = min(i_end, end)
            self.max_k = max(self.events[i][FREQ], self.max_k)
            self.events[i:i] = [[start, self.events[i][START], 1]]
            return self.insert_block(min(end, i_end), max(end, i_end), self.events[i+1][FREQ] - 1 if i_end > i else 1)

        self.events[i:i] = [[start, end, freq]]
        return self.max_k

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
if __name__ == '__main__':
    c = MyCalendarThree()
    for start, end in [[8,23],[35,48],[24,39],[10,22],[10,23],[8,22],[1,14],[36,50],[42,50],[42,50]]:
        print(c.book(start, end))
    # print(c.book(0,2))
    # print(c.book(2,4))
    # print(c.book(0,4))
    # print(c.book(5,10))
    # print(c.book(5,7))
    # print(c.book(15,20))
    # print(c.book(11,20))
    pass