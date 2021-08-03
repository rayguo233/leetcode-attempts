// https://leetcode-cn.com/contest/weekly-contest-232/problems/maximum-score-of-a-good-subarray/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int maximumScore(const vector<int>& nums, const int k) {
        int l = k-1, r = k+1;
        const int size = nums.size();
        int curr_min = nums.at(k);
        int res = curr_min;
        while (l >= 0 || r < size) {
            if (r >= size || (l >= 0 && r < size && nums.at(l) > nums.at(r))) {
                curr_min = min(curr_min, nums.at(l));
                res = max(res, curr_min * (r - l));
                l--;
                continue;
            }
            curr_min = min(curr_min, nums.at(r));
            res = max(res, curr_min * (r - l));
            r++;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
}