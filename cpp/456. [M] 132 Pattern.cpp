// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <stack>

using namespace std;;

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<pair<int, int>> s;
        for (int n : nums) {
            if (s.empty() || n < s.top().first) {
                s.push({n, n});
                continue;
            }

            if (n == s.top().first)
                continue;

            int bottom = s.top().first;
            while (!s.empty() && n >= s.top().second) {
                s.pop();
            }

            if (!s.empty() && s.top().first < n)
                return true;

            s.push({bottom, n});
        }
        return false;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
}