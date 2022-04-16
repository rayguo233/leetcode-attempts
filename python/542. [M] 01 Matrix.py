from typing import List


class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        curr_step, next_step = [], []
        nrow, ncol = len(mat), len(mat[0])
        num_steps = 1
        for r in range(nrow):
            for c in range(ncol):
                cell = mat[r][c]
                if cell == 0:
                    curr_step.append((r, c))
                else:
                    mat[r][c] = -1

        while curr_step:
            next_step = []
            for r, c in curr_step:
                for next_r, next_c in [(r + 1, c), (r - 1, c), (r, c + 1),
                                       (r, c - 1)]:
                    if not (0 <= next_r < nrow and 0 <= next_c < ncol
                            and mat[next_r][next_c] == -1):
                        continue
                    mat[next_r][next_c] = num_steps
                    next_step.append((next_r, next_c))
            num_steps += 1
            curr_step = next_step
        return mat


if __name__ == '__main__':
    sol = Solution()
    print(1)
    print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
