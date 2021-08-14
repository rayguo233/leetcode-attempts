#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    string largestNumber_too_much_mem(vector<int>& nums) {
        vector<string> arr[10];
        for (int n : nums) {
            string num = to_string(n);
            arr[num[0] - '0'].push_back(num);
        }
        auto compare = [](const string &a, const string &b) -> bool {
            return a+b > b+a;
        };
        string res = "";
        for (int i = 9; i >= 0; i--) {
            vector<string> v = arr[i];
            sort(v.begin(), v.end(), compare);
            for (string s : v) {
                res += s;
            }
        }
        return res;
    }

    string largestNumber(const vector<int>& nums) {
        vector<string> vs;
        vs.reserve(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            vs.push_back(to_string(nums[i]));
        }
        auto compare = [](const string &a, const string &b) -> bool {
            return a+b > b+a;
        };
        sort(vs.begin(), vs.end(), compare);
        string res = "";
        for (string s : vs) {
            res += s;
        }
        if (res.size() && res[0] == '0')
            return "0";
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {10,2};
    sol.largestNumber(input);
}