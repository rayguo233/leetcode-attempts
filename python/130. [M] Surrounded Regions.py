from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows, ncols = len(board), len(board[0])

        def mark_safe(r: int, c: int) -> None:
            if ((not 0 <= r < nrows) or (not 0 <= c < ncols) or board[r][c] != 'O'):
                return
            board[r][c] = 'Y'
            for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                mark_safe(i, j)
        
        for r in [0, nrows - 1]:
            for c in range(ncols):
                mark_safe(r, c)
        for r in range(nrows):
            for c in [0, ncols - 1]:
                mark_safe(r, c)
        
        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'Y':
                    board[r][c] = 'O'


        
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxAreaOfIsland([[1,0],[0,0]]))
    print(sol.maxAreaOfIsland([[1,0,1],[0,0,1]]))
