// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <utility>
#include <algorithm>

using namespace std;;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int nrow = matrix.size();
        int ncol = matrix[0].size();
        int countUp[ncol];
        int countLeft[ncol];
        int prevRowMaximalSquare[ncol];
        int currRowMaximalSquare[ncol];
        int* prevRow = prevRowMaximalSquare;
        int* currRow = currRowMaximalSquare;
        int maxSideLen = 0;

        for (int r = 0; r < nrow; r++) {
            for (int c = 0; c < ncol; c++) {
                if (matrix[r][c] == '0') {
                    countUp[c] = 0;
                    countLeft[c] = 0;
                    currRow[c] = 0;
                    continue;
                }

                maxSideLen = max(maxSideLen, 1);
                currRow[c] = 1;

                if (r == 0 && c == 0) {
                    countUp[c] = 1;
                    countLeft[c] = 1;
                } else if (r == 0) {
                    countUp[c] = 1;
                    countLeft[c] = countLeft[c-1] + 1;
                } else if (c == 0) {
                    countUp[c]++;
                    countLeft[c] = 1;
                } else {
                    countUp[c]++;
                    countLeft[c] = countLeft[c-1] + 1;
                    int findMin[] = {prevRow[c-1] + 1, countUp[c], countLeft[c]};
                    currRow[c] = *min_element(findMin, findMin+3);
                    maxSideLen = max(maxSideLen, currRow[c]);
                }
            }
            swap(currRow, prevRow);
        }
        return maxSideLen * maxSideLen;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
}