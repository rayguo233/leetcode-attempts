from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        starts = deque([1])  # type: deque[int]
        steps = 0
        n = len(board)
        dist_to_visited = [False for _ in range(n ** 2 + 1)]
        dist_to_visited[1] = True
        if n == 1: return 0
        while starts:
            steps += 1
            # print(steps, starts)
            for _ in range(len(starts)):
                start = starts.popleft()
                for move in range(1, 7):
                    dist = start + move
                    square = self.get_square_by_distance(dist, board)
                    destination = square if square != -1 else dist
                    if destination >= n ** 2:
                        return steps
                    if dist_to_visited[destination]:
                        continue
                    dist_to_visited[dist] = True
                    dist_to_visited[destination] = True
                    if square != -1:
                        # print(start, dist, square)
                        dist_to_visited[square] = True
                        starts.append(square)
                    else:
                        # print(start, dist, move, square, self.get_xy(dist, len(board)))
                        starts.append(dist)
        return -1

    def get_square_by_distance(self, distance, board) -> int:
        n = len(board)
        if not 1 <= distance <= n ** 2:
            return -1
        x, y = self.get_xy(distance, n)
        return board[y][x]

    def get_xy(self, distance: int, n: int) -> Tuple[int, int]:
        y = n - ((distance - 1) // n) - 1
        x = (distance - 1) % n
        if not (n - y) % 2:
            x = n - 1 - x
        return x, y


if __name__ == '__main__':
    sol = Solution()
    # print(sol.get_xy(1, 6), 0, 5)
    # print(sol.get_xy(7, 3), 0, 0)
    # print(sol.get_xy(6, 6), 5, 5)
    # print(sol.get_xy(7, 6), 5, 4)
    # print(sol.get_xy(12, 6), 0, 4)
    # print(sol.snakesAndLadders([[-1]]))
    # print(sol.snakesAndLadders([[1,1,-1],
    #                             [1,1,1],
    #                             [-1,1,1]]), -1)
    # print(sol.snakesAndLadders([[-1,-1],[-1,-1]]))
    print(sol.snakesAndLadders([[-1,10,-1,15,-1],
                                [-1,-1,18,2,20],
                                [-1,-1,12,-1,-1],
                                [2,4,11,18,8],
                                [-1,-1,-1,-1,-1]]))
    # print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
