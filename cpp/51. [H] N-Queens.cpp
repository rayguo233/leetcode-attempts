#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

#define SolveNQueens solveNQueens

class Solution {
public:
    vector<vector<string>> SolveNQueens(int n) {
        is_row_valid_.resize(n, true);
        is_col_valid_.resize(n, true);
        is_upper_left_valid_.resize(3 * n - 2, true);
        is_upper_right_valid_.resize(3 * n - 2, true);
        n_ = n;
        TryRow(0);
        return string_sol_;
    }
private:
    vector<vector<string>> string_sol_;
    vector<pair<int, int>> int_sol_;
    vector<bool> is_row_valid_;
    vector<bool> is_col_valid_;
    vector<bool> is_upper_left_valid_;
    vector<bool> is_upper_right_valid_;
    int n_;
    void TryRow(int r) {
        if (r >= n_)
            return;
        for (int c = 0; c < n_; c++) {
            if (!IsValid(r, c))
                continue;
            Mark(r, c);
            TryRow(r + 1);
            Backtrack(r, c);
            // break;
        }
    }
    bool IsValid(int r, int c) {
        return is_row_valid_[r]       
            && is_col_valid_[c]
            && is_upper_left_valid_[(c - r) + n_ - 1]
            && is_upper_right_valid_[c + r];
    }
    void Mark(int r, int c) {
        is_row_valid_[r] = false;        
        is_col_valid_[c] = false;        
        is_upper_left_valid_[(c - r) + n_ - 1] = false;
        is_upper_right_valid_[c + r] = false;
        int_sol_.push_back({r, c});
        if (r == n_ - 1)
            DrawSolution();
    }
    void Backtrack(int r, int c) {
        is_row_valid_[r] = true;        
        is_col_valid_[c] = true;        
        is_upper_left_valid_[(c - r) + n_ - 1] = true; 
        is_upper_right_valid_[c + r] = true;
        int_sol_.pop_back();
    }
    void DrawSolution() {
        vector<string> board(n_, string(n_, '.'));
        for (auto &p : int_sol_) {
            board[p.first][p.second] = 'Q';
        }
        string_sol_.push_back(board);
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<int> ::iterator ptr;
}