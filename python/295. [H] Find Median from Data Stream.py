import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        assert len(self.min_heap) >= len(self.max_heap)
        if (not self.min_heap) or (not self.max_heap):
            heapq.heappush(self.min_heap, num)
        elif num <= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) == len(self.min_heap) - 2:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        assert len(self.min_heap) >= len(self.max_heap)
        if len(self.min_heap) == len(self.max_heap):
            return (float(self.min_heap[0]) - self.max_heap[0]) / 2
        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == '__main__':
    sol = Solution()
    a = [2, 0]
    a = [0]
    a = [1, 2]
    a = [1, 0, 2]
    sol.sortColors(a)
    print(a)
    # print(sol.sortColors("a", 'aa'))
    # print(sol.minWindow_clean("ASDF", ''))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
