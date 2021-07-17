#include <vector>  
#include <iostream>
#include <climits>

using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>> &grid) {
        int nrow = grid.size();
        if (nrow == 0)
            return 0;
        int ncol = grid[0].size();
        if (ncol == 0)
            return 0;
        if (grid[0][0] == 1)
            return -1;
        for (int r = 0; r < nrow; r++) {
            for (int c = 0; c < ncol; c++)
                if (grid[r][c] == 1)
                    grid[r][c] = INT_MAX;
        }
        grid[0][0] = 1;
        vector<pair<int, int>> stack = {{0,0}};
        vector<pair<int, int>> nextStack;

        while (stack.size() > 0) {
            nextStack = {};
            while (stack.size() > 0) {
                auto currCell = stack.back();
                stack.pop_back();
                markAndGet(grid, nextStack, grid[currCell.first][currCell.second], nrow, ncol, currCell.first-1, currCell.second);
                markAndGet(grid, nextStack, grid[currCell.first][currCell.second], nrow, ncol, currCell.first-1, currCell.second-1);
                markAndGet(grid, nextStack, grid[currCell.first][currCell.second], nrow, ncol, currCell.first-1, currCell.second+1);
                markAndGet(grid, nextStack, grid[currCell.first][currCell.second], nrow, ncol, currCell.first+1, currCell.second);
                markAndGet(grid, nextStack, grid[currCell.first][currCell.second], nrow, ncol, currCell.first+1, currCell.second-1);
                markAndGet(grid, nextStack, grid[currCell.first][currCell.second], nrow, ncol, currCell.first+1, currCell.second+1);
                markAndGet(grid, nextStack, grid[currCell.first][currCell.second], nrow, ncol, currCell.first, currCell.second+1);
                markAndGet(grid, nextStack, grid[currCell.first][currCell.second], nrow, ncol, currCell.first, currCell.second-1);
            }
            stack.swap(nextStack);
        }

        if (grid[nrow-1][ncol-1] == INT_MAX || grid[nrow-1][ncol-1] == 0)
            return -1;
        return grid[nrow-1][ncol-1];
    }
private:
    void markAndGet(vector<vector<int>> &grid, vector<pair<int, int>> &nextStack, int cellVal, int nrow, int ncol, int r, int c) {
        if (r < 0 || r >= nrow || c < 0 || c >= ncol || grid[r][c] == INT_MAX || (grid[r][c] <= cellVal + 1 && grid[r][c] > 0))
            return;
        grid[r][c] = cellVal + 1;
        nextStack.push_back({r, c});
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> grid = {{0,1},{1,0}};
    cout << sol.shortestPathBinaryMatrix(grid) << endl;
    cout << grid[0][0] << ' ' << grid[1][1] << endl;
}