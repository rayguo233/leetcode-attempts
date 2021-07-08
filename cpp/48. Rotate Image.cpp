// https://leetcode.com/problems/rotate-image/

#include <vector>
#include <iostream>
#include <math.h>

using namespace std;;

#define ROW 0
#define COL 1

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        float center[2];
        center[ROW] = (matrix.size() / 2.) - 0.5;
        if (center[ROW] == 0)
            return;
        center[COL] = (matrix[0].size() / 2.) - 0.5;
        for (int r = 0; r < center[ROW]; r++) {
            for (int c = 0; c <= center[COL]; c++) {
                rotateCells(matrix, r, c, center);
            }
        }
    }

    void rotateCells(vector<vector<int>>& matrix, int r, int c, float center[2]) {
        int prev = matrix[r][c];
        int curr;
        int newCoord[2];
        // rotate four times
        for (int i = 0; i < 4; i++) {
            rotateCellCoordinates(r, c, center, newCoord);
            r = newCoord[ROW];
            c = newCoord[COL];
            curr = matrix[r][c];
            matrix[r][c] = prev;
            prev = curr;
        }
    }

    void rotateCellCoordinates(int r, int c, float center[2], int newCoord[2]) {
        newCoord[ROW] = center[ROW] + (c - center[COL]);
        newCoord[COL] = center[COL] - (r - center[ROW]);
    }

    void printRes(vector<vector<int>> &matrix) {
        rotate(matrix);
        
        int nrow = matrix.size();
        if (nrow == 0) {
            return;
        }
        int ncol = matrix[0].size();

        for (int r = 0; r < nrow; r++) {
            for (int c = 0; c < ncol; c++) {
                cout << matrix[r][c] << ' ';
            }
            cout << endl;
        }
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> a;
    a = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
    // a = {{1,2,3,4},{4,5,6},{7,8,9}};
    sol.printRes(a);
    // float b[2] = {1,1};
    // int c[2];
    // sol.rotateCellCoordinates(0, 1, b, c);
    // cout << c[ROW] << c[COL] << endl;
}