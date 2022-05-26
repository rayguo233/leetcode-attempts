from heapq import heappop, heappush
from typing import List


class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_num_ppl = 0
        heap = []
        trips.sort(key=lambda x: (x[1], x[2]))
        for num_ppl, frm, to in trips:
            while heap and heap[0][0] <= frm:
                drop_pos, num_ppl_to_drop = heappop(heap)
                curr_num_ppl -= num_ppl_to_drop
            curr_num_ppl += num_ppl
            if curr_num_ppl > capacity:
                return False
            heappush(heap, (to, num_ppl))
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.carPooling([[2, 3, 5], [2, 0, 1], [2, 2, 4]], 4))
