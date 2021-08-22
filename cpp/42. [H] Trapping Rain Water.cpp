// https://leetcode.com/problems/rotate-image/

#include <vector>
#include <iostream>
#include <math.h>
#include <stack>

using namespace std;;

#define ROW 0
#define COL 1

class Solution {
public:
    int Trap(const vector<int>& height) {
        int res = 0;
        stack<pair<int, int>> left_walls;
        for (int i = 0; i < height.size(); i++) {
            int h = height[i];
            while (!left_walls.empty() && left_walls.top().first < h) {
                int base = left_walls.top().first;
                left_walls.pop();
                if (left_walls.empty())
                    break;
                res += (i - left_walls.top().second) * min(left_walls.top().first - base, h - base);
            }
            if (!left_walls.empty() && left_walls.top().first == h)
                continue;
            left_walls.push({h, i});

        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    stack<int> s;
    // float b[2] = {1,1};
    // int c[2];
    // sol.rotateCellCoordinates(0, 1, b, c);
    // cout << c[ROW] << c[COL] << endl;
}