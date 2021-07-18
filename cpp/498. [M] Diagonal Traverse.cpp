// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int nrows = mat.size();
        if (nrows == 0)
            return {};
        int ncols = mat[0].size();
        if (ncols == 0)
            return {};
        
        vector<int> res = {};
        res.reserve(nrows*ncols);
        int go_up = 1;
        int row = 0, col = 0;
        while (true) {
            if (row == nrows-2 && col == ncols)
                break;
            if (row == nrows && col == ncols-2)
                break;
            if (go_up == 1 && col == ncols) {
                go_up = -1;
                col -= 1;
                row += 2;
            } else if (go_up == -1 && row == nrows) {
                go_up = 1;
                col += 2;
                row -= 1;
            }
            // if ((row < 0 && col >= ncols) || (row >= nrows && col < 0)) {
            //     go_up = -go_up;
            //     row -= go_up;
            //     col += go_up;
            //     if (go_up == 1)
            //         col += go_up;
            //     else 
            //         row -= go_up;
            // } else 
            else if (row < 0 || row >= nrows) {
                go_up = -go_up;
                row -= go_up;
                if (col < 0 || col >= ncols) {
                    row -= go_up;
                    col += go_up;
                }
            } else if (col < 0 || col >= ncols) {
                go_up = -go_up;
                col += go_up;
                // if (row < 0 || row >= nrows) {
                //     row -= go_up;
                //     col += go_up;
                // }
            } else {
                res.push_back(mat[row][col]);
                row -= go_up;
                col += go_up;
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> input = {{1,2},{3,4},{5,6}};
    input = {{1,2},{3,4}};
    input = {{1,2},{3,4},{5,6}};
    auto res = sol.findDiagonalOrder(input);
    cout << res.size() << endl;
    for (int a : res)
        cout << a << ' ';
    cout << endl;
}