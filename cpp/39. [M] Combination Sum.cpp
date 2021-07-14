
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        int size = candidates.size();
        vector<vector<int>> res;
        for (int i = 0; i < size; i++) {
            vector<vector<int>> comb = recursiveFindSum(candidates, target, i, size);
            if (comb.size() > 0) {
                for (auto v : comb)
                    res.push_back(v);
            }
        }
        return res;
    }
private:
    vector<vector<int>> recursiveFindSum(const vector<int> &nums, const int target, const int i, const int size) {
        if (target <= 0 || i >= nums.size())
            return {};
        if (i > 0 && nums[i] == nums[i-1])
            return {};
        if (target == nums[i])
            return {{nums[i]}};
        vector<vector<int>> res;
        const int need = target - nums[i];
        for (int j = i; j < size; j++) {
            auto comb = recursiveFindSum(nums, need, j, size);
            // if target sum found
            if (comb.size() != 0)
                for (auto v : comb) {
                    v.push_back(nums[i]);
                    res.push_back(v);
                }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {2,3,5};
    auto res = sol.combinationSum(a, 8);
    for (auto v : res) {
        for (int n : v)
            cout << n << ' ';
        cout << endl;
    }
}