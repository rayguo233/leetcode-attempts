// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        for (int a : asteroids) {
            if (a > 0 || stack.empty()) {
                stack.push_back(a);
                continue;
            }
            while (!stack.empty() && stack.back() > 0 && (stack.back() + a < 0))
                stack.pop_back();
            if (stack.empty() || stack.back() < 0) {
                stack.push_back(a);
                continue;
            }
            if (stack.back() + a == 0) {
                stack.pop_back();
            }
        }
        return stack;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {1,2,3,4,-4,-3, -4};
    auto res = sol.asteroidCollision(a);
    for (int i : res) {
        cout << i << ' ';
    }
    cout << endl;
}