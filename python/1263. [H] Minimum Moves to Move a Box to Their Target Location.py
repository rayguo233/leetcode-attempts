from typing import List, Tuple


class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        steps = 0
        nrows, ncols = len(grid), len(grid[0])
        player_row0, player_col0 = self.get_val_pos(grid, 'S')
        box_row0, box_col0 = self.get_val_pos(grid, 'B')
        curr_level = [((box_row0, box_col0), (player_row0, player_col0))]
        visited = set(curr_level)
        while curr_level:
            # print(curr_level)
            next_level = []
            for (box_row, box_col), (player_row, player_col) in curr_level:
                for (box_row1, box_col1), (player_row1, player_col1) in [
                    ((box_row + 1, box_col), (box_row - 1, box_col)),
                    ((box_row - 1, box_col), (box_row + 1, box_col)),
                    ((box_row, box_col + 1), (box_row, box_col - 1)),
                    ((box_row, box_col - 1), (box_row, box_col + 1)),
                ]:
                    if not (0 <= box_row1 < nrows and 0 <= box_col1 < ncols
                            and 0 <= player_row1 < nrows
                            and 0 <= player_col1 < ncols):
                        continue
                    if grid[box_row1][box_col1] == '#' or grid[player_row1][
                            player_col1] == '#':
                        continue
                    if not self.keeper_can_move_here(
                            grid, player_row, player_col, player_row1,
                            player_col1, box_row, box_col):
                        continue
                    if grid[box_row1][box_col1] == 'T':
                        return steps + 1
                    next_level.append(
                        ((box_row1, box_col1), (player_row1, player_col1)))
                    visited.add(
                        ((box_row1, box_col1), (player_row1, player_col1)))
            steps += 1
            curr_level = next_level
        return -1

    def keeper_can_move_here(self, grid: List[List[str]], row0, col0, row1,
                             col1, box_row, box_col) -> bool:
        if row0 == row1 and col0 == col1:
            return True
        nrows, ncols = len(grid), len(grid[0])
        if not (0 <= row0 < nrows and 0 <= col0 < ncols and 0 <= row1 < nrows
                and 0 <= col1 < ncols):
            return False
        stack = [(row0, col0)]
        visited = set(stack)
        while stack:
            curr_row, curr_col = stack.pop()
            for next_row, next_col in [(curr_row + 1, curr_col),
                                       (curr_row - 1, curr_col),
                                       (curr_row, curr_col + 1),
                                       (curr_row, curr_col - 1)]:
                if not (0 <= next_row < nrows and 0 <= next_col < ncols):
                    continue
                if ((next_row, next_col)
                        in visited) or grid[next_row][next_col] == '#' or (
                            next_row == box_row and next_col == box_col):
                    continue
                if next_row == row1 and next_col == col1:
                    return True
                visited.add((curr_row, curr_col))
                stack.append((next_row, next_col))
        return False

    def get_val_pos(self, grid, val: str) -> Tuple[int, int]:
        for row, cells in enumerate(grid):
            for col, value in enumerate(cells):
                if value == val:
                    return row, col


if __name__ == '__main__':
    sol = Solution()
    print(
        sol.minPushBox([["#", "#", "#", "#", "#", "#"],
                        ["#", "T", ".", ".", "#", "#"],
                        ["#", ".", "#", "B", ".", "#"],
                        ["#", ".", ".", ".", ".", "#"],
                        ["#", ".", ".", ".", "S", "#"],
                        ["#", "#", "#", "#", "#", "#"]]))
    print(
        sol.minPushBox([["#", "#", "#", "#", "#", "#"],
                        ["#", "T", "#", "#", "#", "#"],
                        ["#", ".", ".", "B", ".", "#"],
                        ["#", "#", "#", "#", ".", "#"],
                        ["#", ".", ".", ".", "S", "#"],
                        ["#", "#", "#", "#", "#", "#"]]))
    print(
        sol.minPushBox([["#", "#", "#", "#", "#", "#"],
                        ["#", "T", "#", "#", "#", "#"],
                        ["#", ".", ".", "B", ".", "#"],
                        ["#", ".", "#", "#", ".", "#"],
                        ["#", ".", ".", ".", "S", "#"],
                        ["#", "#", "#", "#", "#", "#"]]))
