import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[0, 0]]] * length
        self.len = length
        self.latest_snap = -1

    def set(self, index: int, val: int) -> None:
        self.arr[index][-1][1] = val

    def snap(self) -> int:
        self.latest_snap += 1
        for i in range(self.len):
            if len(self.arr[i]) > 1 and self.arr[i][-1][1] == self.arr[i][-2][1]:
                self.arr[i][-2][0] = self.latest_snap
            else:
                self.arr[i][-1][0] = self.latest_snap
                self.arr[i].append(self.arr[i][-1])
            self.arr[i][-1][0] = self.latest_snap + 1
        return self.latest_snap

    def get(self, index: int, snap_id: int) -> int:
        ind = bisect.bisect_right(self.arr[index], [snap_id + 1, -1])
        return self.arr[index][ind][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)