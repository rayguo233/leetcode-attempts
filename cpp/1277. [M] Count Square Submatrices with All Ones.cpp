// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int nrows = matrix.size();
        if (nrows == 0)
            return 0;
        int ncols = matrix[0].size();
        if (ncols == 0)
            return 0;
        
        int res = 0;
        vector<int> prev_vertical_ones(ncols, 0);
        vector<int> prev_max_square(ncols, 0);
        int horizontal_ones;

        for (int r = 0; r < nrows; r++) {
            horizontal_ones = 0;
            int prev_diagonal;
            for (int c = 0; c < ncols; c++) {
                if (matrix[r][c] == 0) {
                    prev_vertical_ones[c] = 0;
                    prev_max_square[c] = 0;
                    horizontal_ones = 0;
                    continue;
                }

                horizontal_ones++;                        
                prev_vertical_ones[c]++;
                if (c == 0) {
                    res++;
                    prev_diagonal = prev_max_square[c];
                    prev_max_square[c] = 1;
                    // cout << 1 << endl;
                    continue;
                }

                int curr_max_square = min(prev_diagonal+1, min(horizontal_ones, prev_vertical_ones[c]));
                assert(curr_max_square > 0);
                res += curr_max_square;
                prev_diagonal = prev_max_square[c];
                prev_max_square[c] = curr_max_square;
                // cout << curr_max_square << endl;
            }
        }

        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> a = {{0,1,1,1},{1,1,1,1},{0,1,1,1}};
    cout << sol.countSquares(a) << endl;
}