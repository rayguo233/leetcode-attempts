// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int numTrees(int n) {
        vector<int> memo(n, 0);
        memo[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                memo[i] += memo[j-1] * memo[i-j];
            }
        }
        return memo[n];
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.numTrees(3) << endl;
    cout << sol.numTrees(1) << endl;
}