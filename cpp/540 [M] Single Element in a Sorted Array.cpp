// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        int mid;
        while (l < r) {
            mid = max(l, ((l + r) / 4) * 2);
            if (nums[mid] == nums[mid+1])
                l = mid + 2;
            else if (mid - 1 >= 0 && nums[mid] == nums[mid-1])
                r = mid - 2;
            else
                return nums[mid];
        }
        return nums[l];
    }
};

int main() {
    vector<int> v = {1,1,2,2,3,3,4};
    v = {1,2,2,3,3};
    v = {1,2,2};
    v = {1,1,2};
    v = {2};
    Solution sol = Solution();
    cout << v[sol.singleNonDuplicate(v)] << endl;
}