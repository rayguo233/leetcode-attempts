#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        int targets[] = {0, 1, 2};
        for (int target : targets) {
            while (l <= r) {
                if (nums[l] == target) {
                    l++;
                    continue;
                }
                swap(nums[l], nums[r]);
                r--;
            }
            r = nums.size() - 1;
        }
    }
};

int main() {
    vector<int> v = {0,0,1,2,2,1};
    v = {1,2,2,3,3};
}