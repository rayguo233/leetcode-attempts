// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <stack>

using namespace std;;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int size = temperatures.size();
        vector<int> res(size, 0);
        stack<int> s;
        for (int i = 0; i < size; i++) {
            while (!s.empty() && temperatures.at(s.top()) < temperatures[i]) {
                res.at(s.top()) = i - s.top();
                s.pop();
            }
            s.push(i);
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{1,2},{2,3},{3,4}};
}