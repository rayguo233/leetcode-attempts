// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <math.h>

using namespace std;;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
    }

    bool search(vector<vector<int>>& matrix, int target, int start_r, int end_r,
        int start_c, int end_c, int nrows, int ncols) 
    {
        if (start_r < 0 || start_r >= nrows || start_r > end_r || 
            start_c < 0 || start_c >= ncols || start_c > end_c)
        {
            return false;
        }

        int l = max(start_r, start_c);
        int r = min(end_r, end_c);
        int mid;
        while (l < r) {
            mid = ceil((l + r) / 2.);
            if (matrix[mid][mid] == target)
                return true;
            if (matrix[mid][mid] < target) {
                l = mid;
            } else
                r = mid - 1;
        }
        assert(l == r);
        if (matrix[l][l] > target) {
            
        }
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
}