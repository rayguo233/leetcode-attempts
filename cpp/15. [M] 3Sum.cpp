#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;;

class Solution {
public:
    vector<vector<int>> ThreeSumV1(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int size = nums.size();
        int i = 0;
        vector<vector<int>> res = {};
        // for (auto itr = nums.begin(); itr != nums.end(); itr++) {
        //     cout << *itr << ' ';
        // }
        // cout << endl;

        while (i + 2 < size) {
            int l = i + 1;
            int r = size - 1;
            int sum = nums[i] + nums[l] + nums[r];

            // cout << i << ' ' << l << ' ' << r << endl;
            while (l < r) {
                sum = nums.at(i) + nums.at(l) + nums.at(r);
                if (sum == 0) {
                    // cout << "success" << endl;
                    res.push_back({nums.at(i), nums.at(l), nums.at(r)});
                    int old = nums.at(l);
                    while (l < r && nums.at(l) == old)
                        l++;
                    old = nums.at(r);
                    while (l < r && nums.at(r) == old)
                        r--;
                } else if (sum < 0) {
                    int old = nums.at(l);
                    while (l < r && nums.at(l) == old)
                        l++;
                } else {
                    int old = nums.at(r);
                    while (l < r && nums.at(r) == old)
                        r--;
                }
            }
            // cout << i << ' ' << l << ' ' << r << endl;
            int old = nums.at(i);
            while (i < size && nums.at(i) == old)
                i++;
        }
        return res;
    }

    vector<vector<int>> ThreeSumV2(const vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int nums_size = nums.size();
        for (int i = 0; i < nums_size; i++) {
            if (i > 0 && nums.at(i) == nums.at(i-1))
                continue;
            int first = nums.at(i);
            int second_i = i + 1;
            int third_i = nums_size - 1;
            while (second_i < third_i) {
                if (second_i > i + 1 && nums.at(second_i) == nums.at(second_i-1)) {
                    second_i++;
                    continue;
                }
                if (third_i < nums_size - 1 && nums.at(third_i) == nums.at(third_i+1)) {
                    third_i--;
                    continue;
                }
                int curr_sum = first + nums.at(second_i) + nums.at(third_i);
                if (curr_sum == 0) {
                    res.push_back({first, nums.at(second_i), nums.at(third_i)});
                    second_i++, third_i--;
                } else if (curr_sum < 0) {
                    second_i++;
                } else {
                    third_i--;
                }
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> v = {1,2,3,4,1,1,-1,-1,-2};
    v = {0,0,0};
}