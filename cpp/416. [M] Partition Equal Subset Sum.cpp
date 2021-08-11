#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = 0;
        for (int n : nums)
            total += n;
        if (total % 2 == 1)
            return false;
        vector<bool> dp(total/2 + 1, false);
        dp[0] = true;
        for (int n : nums) {
            for (int i = total/2; i >= n; i--) {
                dp[i] = dp[i] || dp[i-n];
            }
        }
        return dp[total/2];
    }
};

int main() {
    Solution sol = Solution();
    vector<int> v = {1,2,3,6,7,8,9};
    cout << sol.canPartition(v) << endl;
}