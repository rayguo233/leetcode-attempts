#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int nrows = obstacleGrid.size();
        int ncols = obstacleGrid[0].size();
        unordered_map<int, int> m;
        return Traverse(obstacleGrid, 0, 0, nrows-1, ncols-1, m);
    }
private:
    int Traverse(vector<vector<int>> &grid, int x, int y, int xtarget, int ytarget, unordered_map<int, int> &m) {
        int key = x + 1000 * y;
        if (m.find(key) != m.end())
            return m[key];
        if (x < 0 || x > xtarget || y < 0 || y > ytarget || grid[x][y])
            return 0;
        if (x == xtarget && y == ytarget)
            return 1;
        m[key] = Traverse(grid, x+1, y, xtarget, ytarget, m) + Traverse(grid, x, y+1, xtarget, ytarget, m);
        return m[key];
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<int> ::iterator ptr;
}