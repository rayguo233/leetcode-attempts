// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& nums, const int first_len, const int second_len) {
        return max(maxSumTwo(nums, first_len, second_len), maxSumTwo(nums, second_len, first_len));
    }
private:
    int maxSumTwo(vector<int>& nums, const int left_len, const int right_len) {
        const int size = nums.size();
        // get left sums
        vector<int> left_max(size - left_len - right_len + 1, 0);
        int l = 0, r = 0;
        int curr_left_sum = 0;
        for (; r < left_len; r++) {
            curr_left_sum += nums[r];
        }
        left_max[l] = curr_left_sum;
        for (l = 1; r < size - right_len; l++, r++) {
            curr_left_sum += nums[r] - nums[l-1];
            left_max.at(l) = max(left_max.at(l - 1), curr_left_sum);
            cout << max(left_max.at(l), curr_left_sum) << ":" << curr_left_sum << " left " << l << endl;
        }
        // get right sums
        vector<int> right_max(size - left_len - right_len + 1, 0);
        l = size - 1, r = size - 1;
        int curr_right_sum = 0;
        for (; r - l < right_len; l--) {
            curr_right_sum += nums[l];
        }
        // cout << curr_right_sum << endl;
        right_max.at(l-left_len+1) = curr_right_sum;
        for (r--; l >= left_len; l--, r--) {
            curr_right_sum += nums[l] - nums[r+1];
            right_max.at(l-left_len) = max(right_max.at(l-left_len+1), curr_right_sum);
            cout << max(right_max.at(l-left_len), curr_right_sum) << ":" << curr_right_sum << " right " << l << endl;
        }
        // find result
        int res = 0;
        for (int i = 0; i <= size - left_len - right_len; i++) {
            res = max(left_max.at(i) + right_max.at(i), res);
        }
        // return res
        cout << res << endl;
        return res;

    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,0,3};
    cout << sol.maxSumTwoNoOverlap(input, 1,2) << endl;
}