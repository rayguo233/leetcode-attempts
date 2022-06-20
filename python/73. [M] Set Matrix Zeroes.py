from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val != 0:
                    continue
                self.mark_zeros(matrix, r, c)
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == '#':
                    matrix[r][c] = 0

    def mark_zeros(self, matrix, r, c) -> None:
        for col, val in enumerate(matrix[r]):
            if val == 0:
                continue
            matrix[r][col] = '#'
        for row in range(len(matrix)):
            if matrix[row][c] == 0:
                continue
            matrix[row][c] = '#'


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance('abc', 'bcd'))
