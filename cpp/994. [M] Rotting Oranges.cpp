
#include <vector>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;;

#define MARK 3

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int nrow = grid.size();
        int ncol = grid[0].size();
        if (ncol == 0)
            return 0;
        int thisRound = 0;
        int numRound = 0;
        while (true) {
            bool possible = false;
            int numFresh = 0;
            for (int r = 0; r < nrow; r++) {
                for (int c = 0; c < ncol; c++) {
                    // if empty
                    if (grid[r][c] == 0)
                        continue;
                    // if fresh
                    if (grid[r][c] == 1 || grid[r][c] == (MARK + thisRound)) {
                        numFresh++;
                        continue;
                    }
                    // if rotten in the previous round
                    if (grid[r][c] == MARK + (!thisRound))
                        grid[r][c] = 2;
                    // if rotten
                    if (grid[r][c] == 2) {
                        // cout << "----" << endl;
                        possible = rotNeighbor(r-1, c, nrow, ncol, grid, thisRound) || possible;
                        possible = rotNeighbor(r+1, c, nrow, ncol, grid, thisRound) || possible;
                        possible = rotNeighbor(r, c-1, nrow, ncol, grid, thisRound) || possible;
                        possible = rotNeighbor(r, c+1, nrow, ncol, grid, thisRound) || possible;
                    }
                }
            }
            if (numFresh == 0)
                return numRound;
            if (!possible)
                return -1;
            numRound++;
            thisRound = !thisRound;
        }
    }
private:
    bool rotNeighbor(int r, int c, int nrow, int ncol, vector<vector<int>>& grid, int thisRound) {
        if (r >= nrow || c >= ncol || r < 0 || c < 0)
            return false;
        if (grid[r][c] == 1) {
            grid[r][c] = MARK + thisRound;
            cout << r << c << endl;
            return true;
        }
        return false;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> a = {{2,1,1},{1,1,0},{0,1,1}};
    cout << sol.orangesRotting(a) << endl;
}