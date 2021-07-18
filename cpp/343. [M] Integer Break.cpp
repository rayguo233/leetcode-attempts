// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int integerBreak(int n) {
        int dp[n+1];
        for (int i = 0; i <= n; i++) {
            int maxi = 0;
            for (int j = 1; j <= i/2; j++) {
                maxi = max(maxi, max(j, dp[j]) * max(i-j, dp[i-j]));
            }
            dp[i] = maxi;
        }
        return dp[n];
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.integerBreak(8) << endl;
    // cout << sol.integerBreak(2) << endl;
    // cout << sol.integerBreak(3) << endl;
    // cout << sol.integerBreak(4) << endl;
}