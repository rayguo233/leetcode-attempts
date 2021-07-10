// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <utility>
#include <algorithm>

using namespace std;;

#define USED '.'

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int nrow = board.size();
        int ncol = board[0].size();
        for (int r = 0; r < nrow; r++) {
            for (int c = 0; c < ncol; c++) {
                if (existAt(board, r, c, nrow, ncol, &word[0]))
                    return true;
            }
        }
        return false;
    }

    bool existAt(vector<vector<char>> &board, int r, int c, int nrow, int ncol, char *ch) {
        if (*ch == '\0')
            return true;
        if (r < 0 || r >= nrow || c < 0 || c >= ncol)
            return false;
        if (board[r][c] != *ch)
            return false;
        board[r][c] = USED;
        bool res = existAt(board, r+1, c, nrow, ncol, ch+1)
            || existAt(board, r-1, c, nrow, ncol, ch+1)
            || existAt(board, r, c+1, nrow, ncol, ch+1)
            || existAt(board, r, c-1, nrow, ncol, ch+1);
        board[r][c] = *ch;
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    string a = "123123";
    char *c = &a[0];
    while (*c != '\0') {
        cout << *c;
        c++;
    }
    cout << endl;
}