from heapq import heappush, heappushpop


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        size = len(heights)
        hp = []
        for i in range(1, size):
            diff = heights[i] - heights[i-1]
            if diff <= 0:
                continue
            if ladders:
                ladders -= 1
                heappush(hp, diff)
            else:
                bricks -= heappushpop(hp, diff)
                if bricks < 0:
                    return i - 1
        return size - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))
    # assert(sol.rob([0]) == 0)
    # assert(sol.rob([2,1,4]) == 6)
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 10)
    # assert(sol.rob([2,1,4,8,9]) == 15)
