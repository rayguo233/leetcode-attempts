// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <math.h>
#include <queue>

using namespace std;;

struct Comp {
    bool operator() (pair<int, int> a, pair<int, int> b) {
        return a.first > b.first;
    }
};

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int size = nums.size();
        if (size == 0)
            return {};
        priority_queue<pair<int, int>, vector<pair<int, int>>, Comp> pq = {};
        vector<int> res(size, -1);
        for (int i = 0; i < size; i++) {
            while (pq.size() > 0 && pq.top().first < nums[i]) {
                res[pq.top().second] = nums[i];
                pq.pop();
            }
            pq.push({nums[i], i});
        }
        for (int i = 0; i < size; i++) {
            while (pq.size() > 0 && pq.top().first < nums[i]) {
                res[pq.top().second] = nums[i];
                pq.pop();
            }
        }
        while (pq.size() > 0) {
            cout << pq.top().first << ' ';
            pq.pop();
        }
        cout << endl;
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,1};
    auto res = sol.nextGreaterElements(input);
    for (int n : res)
        cout << n << ' ';
    cout << endl;
}