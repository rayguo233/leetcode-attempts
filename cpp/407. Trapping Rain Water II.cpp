
#include <vector>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;;

#define FILLED 300

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        int nrows = heightMap.size();
        int ncols = heightMap.at(0).size();
        if (nrows < 3 || ncols < 3)
            return 0;
        
        for (int r = 1; r < nrows-1; r++) {
            for (int c = 1; c < ncols-1; c++) {
                // get surrounding cells higher than current cell


            }
        }
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> a = {{2,1,1},{1,1,0},{0,1,1}};
}