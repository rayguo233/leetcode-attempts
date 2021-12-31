from typing import List, Tuple

UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = set()
        return self.explore_cell(grid, 0, 0, visited)

    def explore_cell(self, grid: List[List[int]], r: int, c: int, visited: set[Tuple[int, int]]) -> bool:
        # print(r, c, visited)
        visited.add((r, c))
        nrow = len(grid)
        ncol = len(grid[0])
        if r == nrow - 1 and c == ncol - 1:
            return True
        for next_r, next_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if (next_r, next_c) in visited:
                continue
            if self.is_valid_next_step(grid, r, c, next_r, next_c) and self.explore_cell(grid, next_r, next_c, visited):
                return True
        return False

    def is_valid_next_step(self, grid, from_r, from_c, to_r, to_c) -> bool:
        nrow = len(grid)
        ncol = len(grid[0])
        if not (0 <= to_r < nrow and 0 <= to_c < ncol):
            return False
        direction = self.get_direction(from_r, from_c, to_r, to_c)
        # print(from_r, from_c, to_r, to_c, direction)
        if direction == UP:
            return grid[from_r][from_c] in [2,5,6] and grid[to_r][to_c] in [2,3,4]
        elif direction == DOWN:
            return grid[from_r][from_c] in [2,3,4] and grid[to_r][to_c] in [2,5,6]
        elif direction == LEFT:
            return grid[from_r][from_c] in [1,3,5] and grid[to_r][to_c] in [1,4,6]
        elif direction == RIGHT:
            return grid[from_r][from_c] in [1,4,6] and grid[to_r][to_c] in [1,3,5]
        return False

    def get_direction(self, from_r, from_c, to_r, to_c) -> int:
        delta_x, delta_y = to_c - from_c, from_r - to_r
        if delta_y == 1:
            return UP
        elif delta_y == -1:
            return DOWN
        elif delta_x == 1:
            return RIGHT
        elif delta_x == -1:
            return LEFT
        raise AssertionError

if __name__ == '__main__':
    pass
    sol = Solution()
    print(sol.hasValidPath([[2,4,3],[6,5,2]]))
