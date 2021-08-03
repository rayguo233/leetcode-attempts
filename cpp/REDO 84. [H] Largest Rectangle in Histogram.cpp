// https://leetcode-cn.com/problems/largest-rectangle-in-histogram/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <stack>

using namespace std;;

#define START 0
#define INDEX 1
#define HEIGHT 2

class Solution {
public:
    int largestRectangleArea(const vector<int>& heights) {
        const int size = heights.size();
        int res = INT_MIN;
        stack<vector<int>> s;
        for (int i = 0; i < size; i++) {
            while (!s.empty() && s.top()[HEIGHT] > heights.at(i)) {
                res = max(res, (i - s.top()[START]) * s.top()[HEIGHT]);
                // cout << res << ";i=" << i << ";height=" << s.top()[HEIGHT] << ";start=" << s.top()[START] << endl;
                s.pop();
            }
            if (s.empty())
                s.push({0, i, heights[i]});
            else if (s.top()[HEIGHT] < heights.at(i))
                s.push({s.top()[INDEX] + 1, i, heights[i]});
            else if (s.top()[HEIGHT] == heights.at(i))
                s.top()[INDEX] = i;
        }
        while (!s.empty()) {
            res = max(res, (size - s.top()[START]) * s.top()[HEIGHT]);
            // cout << res << ";height=" << s.top()[HEIGHT] << endl;
            s.pop();
        }
        assert(res != INT_MIN);
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> v = {2,1,5,6,2,3};
    v = {0,1,0,1};
    cout << sol.largestRectangleArea(v) << endl;
}