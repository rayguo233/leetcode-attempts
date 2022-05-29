import heapq


class StockPrice:

    def __init__(self):
        self.t_to_p = {}
        self.min_hp = []
        self.max_hp = []
        self.recent = 0

    def update(self, timestamp: int, price: int) -> None:
        self.t_to_p[timestamp] = price
        heapq.heappush(self.min_hp, (price, timestamp))
        heapq.heappush(self.max_hp, (-price, timestamp))
        if timestamp > self.recent:
            self.recent = timestamp

    def current(self) -> int:
        return self.t_to_p[self.recent]

    def maximum(self) -> int:
        while -self.max_hp[0][0] != self.t_to_p[self.max_hp[0][1]]:
            heapq.heappop(self.max_hp)
        return -self.max_hp[0][0]

    def minimum(self) -> int:
        while self.min_hp[0][0] != self.t_to_p[self.min_hp[0][1]]:
            heapq.heappop(self.min_hp)
        return self.min_hp[0][0]


if __name__ == '__main__':
    pass