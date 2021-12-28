from typing import List, Tuple
from collections import deque

MOVE_RIGHT = ((0, 1), (0, 1))
MOVE_DOWN = ((1, 0), (1, 0))
ROTATE_CLOCKWISE = ((0, 0), (1, -1))
ROTATE_COUNTERCLOCKWISE = ((0, 0), (-1, 1))
ROW = 0
COL = 1

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque([((0, 0), (0, 1))])  # type: deque[Tuple[Tuple[int, int], Tuple[int, int]]]
        visited = set()  # type: set[Tuple[Tuple[int, int], Tuple[int, int]]]
        num_steps = 0
        while dq:
            num_steps += 1
            print(dq)
            for _ in range(len(dq)):
                pos0, pos1 = dq.popleft()
                for opr0, opr1 in [MOVE_RIGHT, MOVE_DOWN, ROTATE_CLOCKWISE, ROTATE_COUNTERCLOCKWISE]:
                    next_pos0 = (pos0[ROW] + opr0[ROW], pos0[COL] + opr0[COL])
                    next_pos1 = (pos1[ROW] + opr1[ROW], pos1[COL] + opr1[COL])
                    if (next_pos0, next_pos1) in visited:
                        continue
                    if (opr0, opr1) == ROTATE_CLOCKWISE:
                        if not (pos0[ROW] == pos1[ROW] and self.is_valid_pos(pos0[ROW]+1, pos0[COL], grid) and self.is_valid_pos(pos0[ROW]+1, pos0[COL]+1, grid)):
                            continue
                    elif (opr0, opr1) == ROTATE_COUNTERCLOCKWISE:
                        if not (pos0[COL] == pos1[COL] and self.is_valid_pos(pos0[ROW], pos0[COL]+1, grid) and self.is_valid_pos(pos0[ROW]+1, pos0[COL]+1, grid)):
                            continue
                    else:
                        if not (self.is_valid_pos(next_pos0[ROW], next_pos0[COL], grid) and self.is_valid_pos(next_pos1[ROW], next_pos1[COL], grid)):
                            continue
                    if next_pos0 == (n-1, n-2) and next_pos1 == (n-1, n-1):
                        return num_steps
                    dq.append((next_pos0, next_pos1))
                    visited.add((next_pos0, next_pos1))
        return -1

    def is_valid_pos(self, r: int, c: int, grid: List[List[int]]) -> bool:
        n = len(grid)
        return 0 <= r < n and 0 <= c < n and grid[r][c] == 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumMoves([[0,0,0,0,1,1],
                            [1,1,0,0,0,1],
                            [1,1,1,0,0,1],
                            [1,1,1,0,1,1],
                            [1,1,1,0,0,1],
                            [1,1,1,0,0,0]]))
