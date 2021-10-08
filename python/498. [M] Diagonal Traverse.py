from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        nrows, ncols = len(mat), len(mat[0])
        arr = []
        r, c = 0, 0
        right_up = 1  # type: int
        while r + c <= nrows + ncols - 2:
            arr.append(mat[r][c])
            next_sum = r + c + 1
            r -= right_up
            c += right_up
            right_up = - right_up
            if c == ncols:
                c = ncols - 1
                r = next_sum - c
            elif r == -1:
                r = 0
                c = next_sum - r
            elif r == nrows:
                r = nrows - 1
                c = next_sum - r
            elif c == -1:
                c = 0
                r = next_sum - c
            else:
                right_up = - right_up
        return arr

if __name__ == '__main__':
    sol = Solution()
    print(sol.findDiagonalOrder([[0],[1]]))
