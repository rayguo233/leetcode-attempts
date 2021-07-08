// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> map;
            int len = nums.size();
            for (int i = 0; i < len; i++) {
                if (map.count(target - nums[i]) != 0) {
                    return {i, map[target - nums[i]]};
                }
                map[nums[i]] = i;
            }
            assert(false);
        }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<int> ::iterator ptr;
    vector<int> res = sol.twoSum(input, 13);
    for (ptr = res.begin(); ptr < res.end(); ptr++) {
        cout << *ptr << ' ';
    }
    cout << endl;
}