#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <queue>

using namespace std;;

#define ShortestBridge shortestBridge

class Solution {
public:
    int ShortestBridge(vector<vector<int>>& grid) {
        nrows_ = grid.size(), ncols_ = grid[0].size();
        bool found_land = false;
        for (int r = 0; r < nrows_ && !found_land; r++)
            for (int c = 0; c < ncols_ && !found_land; c++)
                found_land = MarkLand(r, c, grid);
        while (!sol_) {
            int len = q_.size();
            for (int i = 0; i < len && !sol_; i++) {
                int r = q_.front().first, c = q_.front().second;
                q_.pop();
                ExpandFromHereToWater(r, c, grid);
            }
        }
        return sol_;
    }
private:
    int nrows_;
    int ncols_;
    int sol_ = 0;
    queue<pair<int, int>> q_;
    bool is_valid_coord(int r, int c) {
        return 0 <= r && r < nrows_ && 0 <= c && c < ncols_;
    }
    bool MarkLand(int r, int c, vector<vector<int>>& grid) {
        if (!is_valid_coord(r, c) || grid[r][c] != 1)
            return false;
        grid[r][c] = 2;
        int neighbors[4][2] = {{r+1, c}, {r-1, c}, {r, c+1}, {r, c-1}};
        for (auto &coord : neighbors) {
            int row = coord[0], col = coord[1];
            MarkLand(row, col, grid);
        }
        ExpandFromHereToWater(r, c, grid);
        return true;
    }
    void ExpandFromHereToWater(int r, int c, vector<vector<int>>& grid) {
        int neighbors[4][2] = {{r+1, c}, {r-1, c}, {r, c+1}, {r, c-1}};
        for (auto &coord : neighbors) {
            int row = coord[0], col = coord[1];
            if (!is_valid_coord(row, col))
                continue;
            if (grid[row][col] == 1) {
                sol_ = grid[r][c] - 2;
            } else if (grid[row][col] == 0) {
                grid[row][col] = grid[r][c] + 1;
                q_.push({row, col});
            }
        }
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<int> ::iterator ptr;
}