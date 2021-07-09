// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <math.h>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int const len = height.size();
        if (len < 2)
            return 0;
        int l = 0;
        int r = len - 1;
        int res = 0;
        int area;
        while (l < r) {
            int hl = height[l];
            int hr = height[r];
            area = min(hl, hr) * (r - l);
            res = max(area, res);
            if (hl < hr)
                l++;
            else if (hl == hr) {
                l++;
                r--;
            }
            else
                r--;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {1,8,6,2,5,4,8,3,7};
    cout << sol.maxArea(a) << endl;
}