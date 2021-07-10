// 

#include <vector>  
#include <math.h>
#include <iostream>
#include <assert.h>

using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int size = nums.size();
        int l = 0, r = size - 1, mid;
        while (l <= r) {
            mid = (l + r) / 2;
            if (target == nums[mid])
                return true;
            if (nums[mid] == nums[r]) {
                r--;
            } else if (nums[mid] == nums[l]) {
                l++;
            } else if (nums[mid] < nums[r]) {
                if (nums[mid] < target && target <= nums[r]) {
                    l = mid + 1;
                } else
                    r = mid;
            } else {
                if (nums[l] <= target && target < nums[mid]) {
                    r = mid;
                } else 
                    l = mid + 1;
            }
        }
        return false;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a;
    a = {3,4,5,1,2};
    a = {1,2,3};
    cout << sol.search(a, 3) << endl;
}