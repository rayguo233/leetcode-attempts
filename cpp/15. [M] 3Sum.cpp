#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
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

    void print_res(vector<int>& nums) {
        vector<vector<int>> res = threeSum(nums);
        for (auto itr = res.begin(); itr != res.end(); itr++) {
            for (auto it = itr->begin(); it != itr->end(); it++) {
                cout << *it << ' ';
            }
            cout << endl;
        }
    }
};

int main() {
    Solution sol = Solution();
    vector<int> v = {1,2,3,4,1,1,-1,-1,-2};
    v = {0,0,0};
    sol.print_res(v);
}