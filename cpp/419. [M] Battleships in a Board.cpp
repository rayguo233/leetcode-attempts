// https://leetcode.com/problems/battleships-in-a-board/

#include <vector>  
#include <iostream>
#include <unordered_map>

using namespace std;


class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int nrows = board.size();
        int ncols = board.at(0).size();
        vector<bool> prev_row(ncols, false);
        bool left_X = false;
        int res = 0;
        for (int r = 0; r < nrows; r ++) {
            left_X = false;
            for (int c = 0; c < ncols; c++) {
                if (board[r][c] == 'X') {
                    if (left_X || prev_row[c])
                        continue;
                    res++;
                    left_X = true;
                    prev_row[c] = true;
                }
                else {
                    left_X = false;
                    prev_row[c] = false;
                }
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<char>> a = {{'X','.','.','X'},{'.','.','.','X'},{'.','.','.','X'}};
    
}