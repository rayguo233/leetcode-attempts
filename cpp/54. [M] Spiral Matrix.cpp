// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <math.h>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int nrow = matrix.size();
        if (nrow == 0)
            return {};
        int ncol = matrix[0].size();
        if (ncol == 0)
            return {};
        
        vector<int> res = {};
        int topR = 0, bottomR = nrow - 1, leftC = 0, rightC = ncol - 1;
        int currR, currC, endR, endC;
        while (rightC - leftC > 0 && bottomR - topR > 0) {
            // traverse upper row left to right
            currR = topR;
            for (currC = leftC; currC <= rightC; currC++) {
                res.push_back(matrix[currR][currC]);
            }

            // traverse right column top down
            currC = rightC;
            for (currR = topR + 1; currR <= bottomR; currR++) {
                res.push_back(matrix[currR][currC]);
            }

            // traverse bottom row right to left
            currR = bottomR;
            for (currC = rightC - 1; currC >= leftC; currC--) {
                res.push_back(matrix[currR][currC]);
            }

            // traverse left column bottom up
            currC = leftC;
            for (currR = bottomR - 1; currR >= topR + 1; currR--) {
                res.push_back(matrix[currR][currC]);
            }

            // prepare for the next iteration
            topR++; bottomR--; leftC++; rightC--;
        }
        cout << topR << bottomR << leftC << rightC << endl;
        if (bottomR == topR && leftC <= rightC) {
            // traverse the row left to right
            currR = topR;
            for (currC = leftC; currC <= rightC; currC++) {
                res.push_back(matrix[currR][currC]);
            }
        } else if (leftC == rightC && bottomR >= topR) {
            // traverse the column top down
            currC = rightC;
            for (currR = topR; currR <= bottomR; currR++) {
                res.push_back(matrix[currR][currC]);
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> a;
    a = {{3},{2}};
    vector<int> b = sol.spiralOrder(a);
    for (int i : b) {
        cout << i << ' ';
    }
}