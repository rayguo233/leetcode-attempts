// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int nrows = mat.size();
        int ncols = mat[0].size();
        for (int r = 0; r < nrows; r++) {
            SortSingleDiagonal(mat, r, 0, min(nrows-r, ncols));
        }
        for (int c = 1; c < ncols; c++) {
            SortSingleDiagonal(mat, 0, c, min(nrows, ncols-c));
        }
        return mat;
    }
private:
    void SortSingleDiagonal(vector<vector<int>> & mat, int r, int c, int size) {
        if (size <= 0)
            return;
        int index = partition(mat, r, c, size);
        SortSingleDiagonal(mat, r, c, index);
        SortSingleDiagonal(mat, r+index+1, c+index+1, size-index-1);
    }

    int partition(vector<vector<int>> & mat, int r, int c, int size) {
        int pivot_val = mat[r][c];
        swap(mat[r][c], mat[r+size-1][c+size-1]);
        int left = 0, right = size - 2;
        while (left <= right) {
            if (mat[r+left][c+left] <= pivot_val) {
                left++;
                continue;
            }
            if (mat[r+right][c+right] < pivot_val) {
                swap(mat[r+left][c+left], mat[r+right][c+right]);
            }
            right--;
        }
        if (mat[r+left][c+left] > pivot_val) {
            swap(mat[r+size-1][c+size-1], mat[r+left][c+left]);
            return left;
        }
        assert(left == size -1);
        return size - 1;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
}