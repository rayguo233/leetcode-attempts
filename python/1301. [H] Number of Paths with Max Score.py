from typing import List, Tuple, Optional
from collections import defaultdict, deque


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        prev_row = []
        for row_i in reversed(range(len(board))):
            row = board[row_i]
            curr_row = [None] * len(row)  # type: List[Optional[Tuple[int, int]]]
            for col_i in reversed(range(len(row))):
                cell = row[col_i]
                if cell in ['X', 'S', 'E']:
                    score = 0
                else:
                    score = int(cell)
                score_to_num_paths = defaultdict(int)
                if cell == 'X':
                    score_to_num_paths[score] = 0
                elif cell == 'S':
                    score_to_num_paths[score] = 1
                else:
                    if row_i < len(board) - 1:
                        self.record_path(score_to_num_paths, prev_row[col_i], score)
                    if col_i < len(row) - 1:
                        self.record_path(score_to_num_paths, curr_row[col_i + 1], score)
                    if row_i < len(board) - 1 and col_i < len(row) - 1:
                        self.record_path(score_to_num_paths, prev_row[col_i + 1], score)
                max_score = max(score_to_num_paths.keys())
                curr_row[col_i] = (max_score, score_to_num_paths[max_score] % (10 ** 9 + 7))
            prev_row = curr_row
            # print(prev_row)
        return list(prev_row[0])

    def record_path(self, score_to_num_paths, score_and_path, score) -> None:
        prev_score, prev_paths = score_and_path
        if prev_paths > 0:
            score_to_num_paths[prev_score + score] += prev_paths
        else:
            score_to_num_paths[0] = 0





if __name__ == '__main__':
    sol = Solution()
    print(sol.pathsWithMaxScore(['E23',
                                 'XXX',
                                 '32S']))
