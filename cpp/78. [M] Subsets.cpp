#include <vector>  
#include <iostream>
#include <map>
#include <iterator>

using namespace std;

#define num_smaller(itr) (itr->second.first)
#define num_larger(itr) (itr->second.second)

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        return Helper(nums, 0, nums.size());
    }
private:
    vector<vector<int>> Helper(vector<int> &nums, int start, int size) {
        if (start == size)
            return {{}};
        vector<vector<int>> res;
        auto partial_res = Helper(nums, start+1, size);
        for (auto v : partial_res) {
            res.push_back(v);
            v.push_back(nums[start]);
            res.push_back(v);
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {};
}