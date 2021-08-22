// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    bool IncreasingTriplet(const vector<int>& nums) {
        int num_i = INT_MAX, num_j = INT_MAX;
        // int first_i = INT_MAX, first_j = INT_MAX;
        // int second_i = INT_MAX, second_j = INT_MAX;
        for (int n : nums) {
            if (n > num_j)
                return true;
            if (n > num_i)
                num_j = min(num_j, n);
            else
                num_i = min(num_i, n);
        }
        return false;
    }
};

int main() {
    Solution sol = Solution();
    // cout << sol.integerBreak(8) << endl;
    // cout << sol.integerBreak(2) << endl;
    // cout << sol.integerBreak(3) << endl;
    // cout << sol.integerBreak(4) << endl;
}