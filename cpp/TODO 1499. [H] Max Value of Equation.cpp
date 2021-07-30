#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;;

class Solution {
public:
    int findMaxValueOfEquation(const vector<vector<int>>& points, int k) {
        int res = INT_MIN;
        int fp = 0, sp = 1;
        while (fp < points.size() || sp < points.size()) {
            if (sp == points.size() || points[sp][0] - points[fp][0] > k) {
                fp++;
                sp = fp + 1;
                continue;
            }
            res = max(res, points[sp][0] - points[fp][0] + points[sp][1] + points[fp][1]);
            sp++;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> v = {1,2,3,4,1,1,-1,-1,-2};
    v = {0,0,0};
}