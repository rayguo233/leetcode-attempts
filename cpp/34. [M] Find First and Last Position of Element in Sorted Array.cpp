
#include <vector>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size() == 0)
            return {-1,-1};
        vector<int> res;
        int left = 0, right = nums.size() - 1;
        // find left
        int mid;
        while (left < right) {
            mid = (left + right) / 2;
            if (nums[mid] >= target) {
                right = mid;
                continue;
            }
            left = mid + 1;
        }
        if (nums[left] != target)
            return {-1, -1};
        res.push_back(left);
        // find right
        left = 0, right = nums.size() - 1;
        while (left < right) {
            mid = ceil((left + right) / 2.);
            if (nums[mid] <= target) {
                left = mid;
                continue;
            }
            right = mid - 1;
        }
        if (nums[right] != target)
            return {-1, -1};
        res.push_back(right);
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {1,2,4,6,8,8,8};
}