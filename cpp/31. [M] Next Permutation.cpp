#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>

using namespace std;;

// Constraints:

// 1 <= nums.length <= 100
// 0 <= nums[i] <= 100

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        if (len == 1)
            return;
        assert(len > 1);
        vector<int>::iterator max = nums.end() - 1;
        for (auto itr = nums.end() - 2; itr >= nums.begin(); itr--) {
            if (*max > *itr) {
                swap(max, itr);
                return;
            }
            if (*itr > *max) {
                max = itr;
            }
        }
        swap(nums.begin(), nums.end() - 1);
    }

    void swap(vector<int>::iterator a, vector<int>::iterator b) {
        int temp = *a;
        *a = *b;
        *b = temp;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {1,2,3,4,5,6};
    sol.nextPermutation(a);
    for (int i: a) {
        cout << i << ' ';
    }
    cout << endl;
}