from typing import List, Tuple
from collections import deque

ROW = 0
COL = 1
FORWARD_DATA = 0
BACKWARD_DATA = 1
DQ = 0
VISITED = 1

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque([((0, 0), (0, 1))])  # type: deque[Tuple[Tuple[int, int], Tuple[int, int]]]
        visited = {}  # type: dict[Tuple[Tuple[int, int], Tuple[int, int]], int]
        num_steps = 0
        data_sets = [[], []]
        data_sets[FORWARD_DATA].append(deque([((0, 0), (0, 1))]))
        data_sets[BACKWARD_DATA].append(deque([((n-1, n-2), (n-1, n-1))]))
        data_sets[FORWARD_DATA].append({((0, 0), (0, 1)): 0})
        data_sets[BACKWARD_DATA].append({((n-1, n-2), (n-1, n-1)): 0})
        data_sets[FORWARD_DATA].append(((0, 1), (0, 1)))  # MOVE_RIGHT
        data_sets[FORWARD_DATA].append(((1, 0), (1, 0)))  # MOVE_DOWN
        data_sets[FORWARD_DATA].append(((0, 0), (1, -1)))  # ROTATE_CLOCKWISE
        data_sets[FORWARD_DATA].append(((0, 0), (-1, 1)))  # ROTATE_COUNTERCLOCKWISE
        data_sets[BACKWARD_DATA].append(((0, -1), (0, -1)))  # MOVE_RIGHT
        data_sets[BACKWARD_DATA].append(((-1, 0), (-1, 0)))  # MOVE_DOWN
        data_sets[BACKWARD_DATA].append(((0, 0), (-1, 1)))  # ROTATE_CLOCKWISE
        data_sets[BACKWARD_DATA].append(((0, 0), (1, -1)))  # ROTATE_COUNTERCLOCKWISE
        while data_sets[FORWARD_DATA][DQ] or data_sets[BACKWARD_DATA][DQ]:
            num_steps += 1
            for direction, data_set in enumerate(data_sets):
                dq, visited, MOVE_RIGHT, MOVE_DOWN, ROTATE_CLOCKWISE, ROTATE_COUNTERCLOCKWISE = data_set
                print(dq)
                for _ in range(len(dq)):
                    pos0, pos1 = dq.popleft()
                    for opr0, opr1 in [MOVE_RIGHT, MOVE_DOWN, ROTATE_CLOCKWISE, ROTATE_COUNTERCLOCKWISE]:
                        next_pos0 = (pos0[ROW] + opr0[ROW], pos0[COL] + opr0[COL])
                        next_pos1 = (pos1[ROW] + opr1[ROW], pos1[COL] + opr1[COL])
                        if (next_pos0, next_pos1) in visited:
                            continue
                        if (opr0, opr1) == ROTATE_CLOCKWISE:
                            if direction == FORWARD_DATA and not (pos0[ROW] == pos1[ROW] and self.is_valid_pos(pos0[ROW]+1, pos0[COL], grid) and self.is_valid_pos(pos0[ROW]+1, pos0[COL]+1, grid)):
                                continue
                            if direction == BACKWARD_DATA and not (pos0[ROW] == pos1[ROW] and self.is_valid_pos(pos0[ROW], pos0[COL]+1, grid) and self.is_valid_pos(pos0[ROW]+1, pos0[COL]+1, grid)):
                                continue
                        elif (opr0, opr1) == ROTATE_COUNTERCLOCKWISE:
                            if direction == FORWARD_DATA and not (pos0[COL] == pos1[COL] and self.is_valid_pos(pos0[ROW], pos0[COL]+1, grid) and self.is_valid_pos(pos0[ROW]+1, pos0[COL]+1, grid)):
                                continue
                            if direction == BACKWARD_DATA and not (pos0[COL] == pos1[COL] and self.is_valid_pos(pos0[ROW]+1, pos0[COL], grid) and self.is_valid_pos(pos0[ROW]+1, pos0[COL]+1, grid)):
                                continue
                        else:
                            if not (self.is_valid_pos(next_pos0[ROW], next_pos0[COL], grid) and self.is_valid_pos(next_pos1[ROW], next_pos1[COL], grid)):
                                continue
                        other_direction = not direction
                        if (next_pos0, next_pos1) in data_sets[other_direction][VISITED]:
                            return num_steps + data_sets[other_direction][VISITED][(next_pos0, next_pos1)]
                        dq.append((next_pos0, next_pos1))
                        visited[(next_pos0, next_pos1)] = num_steps
        return -1

    def is_valid_pos(self, r: int, c: int, grid: List[List[int]]) -> bool:
        n = len(grid)
        return 0 <= r < n and 0 <= c < n and grid[r][c] == 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumMoves([[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]))
