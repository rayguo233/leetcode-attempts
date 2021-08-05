#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        const int nrows = mat.size();
        const int ncols = mat.at(0).size();
        vector<pair<int, int>> last_row(ncols, {0, 0});
        for (int r = 0; r < nrows; r++) {
            int prev_ones = 0;
            pair<int, int> prev_cell = {0, 0};
            for (int c = 0; c < ncols; c++) {
                if (mat[r][c] == 0) {
                    last_row[c] = {0, 0};
                    prev_ones = 0;
                    continue;
                }
                prev_ones++;
                pair<int, int> top_rectgl = {min(last_row[c].first, prev_ones), last_row[c].second + 1};
                // pair<int, int> left_rectgl = {min(), 0};

            }
        }
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<int> ::iterator ptr;
}