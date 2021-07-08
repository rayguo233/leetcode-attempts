
#include <vector>

using namespace std;;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int nrow = grid.size();
        if (nrow == 0)
            return 0;
        int ncol = grid[0].size();
        int res = 0;

        for (int r = 0; r < nrow; r++) {
            for (int c = 0; c < ncol; c++) {
                if (grid[r][c] == '1') {
                    mark(grid, nrow, ncol, r, c);
                    res++;
                } 
            }
        }
        return res;
    }

private:
    void mark(vector<vector<char>>& grid, int nrow, int ncol,
                int r, int c) 
    {
        if (r < 0 || r >= nrow || c < 0 || c >= ncol || grid[r][c] != '1')
            return;
        grid[r][c] = '#';
        mark(grid, nrow, ncol, r-1, c);
        mark(grid, nrow, ncol, r, c-1);
        mark(grid, nrow, ncol, r+1, c);
        mark(grid, nrow, ncol, r, c+1);
    }
};