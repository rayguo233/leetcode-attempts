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
    void nextPermutationV1(vector<int>& nums) {
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
        iter_swap(nums.begin(), nums.end() - 1);
    }

    // void swap(vector<int>::iterator a, vector<int>::iterator b) {
    //     int temp = *a;
    //     *a = *b;
    //     *b = temp;
    // }

    void NextPermutation(vector<int>& nums) {
        const int kNumsSize = nums.size();
        int curr_max = nums[kNumsSize-1];
        int curr_max_ind = kNumsSize - 1;
        for (int i = kNumsSize - 2; i >= 0; i--) {
            int curr_num = nums[i];
            if (curr_num == curr_max)
                continue;
            if (curr_num > curr_max) {
                curr_max = curr_num, curr_max_ind = i;
                continue;
            }
            for (int j = i + 1; j < kNumsSize; j++) {
                if (nums[j] < curr_max && nums[j] > curr_num)
                    curr_max = nums[j], curr_max_ind = j;
            }
            swap(nums[i], nums[curr_max_ind]);
            if (i < kNumsSize - 1)
                sort(nums.begin() + i + 1, nums.end());
        }
        for (int l = 0, r = kNumsSize-1; l <= r; l++, r--)
            swap(nums[l], nums[r]);
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {1,2,3,4,5,6};
    a = {1,1,3,2};
    a = {1,9,7,5,4,3,2,1};

    sol.NextPermutation(a);
    for (int i: a) {
        cout << i << ' ';
    }
    cout << endl;
}