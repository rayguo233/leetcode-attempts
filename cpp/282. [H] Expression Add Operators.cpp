#include <vector>
#include <string>
#include <iostream>

using namespace std;;

#define NULLINT 0

class Solution {
public:
    vector<string> addOperators(const string num, int target) {
        return dfs(num, 0, false, false, NULLINT, target);
    }
private:
    vector<string> dfs(const string num, const int start, bool prev_is_minus,
        bool prev_is_mult, int prev_mult_val, int target) 
    {
        // cout << num << ": " << start << "; " << target << endl;
        // assert(start <= num.size());
        assert(!prev_is_minus || !prev_is_mult);
        // if (start == num.size() && target == 0 && !prev_is_minus && !prev_is_mult)
        //     return {""};
        if (start >= num.size())
            return {};

        vector<string> res;
        for (int len = 1; len <= num.size() - start; len++) {
            // cout << start << " " << len << endl;
            long int val = stol(num.substr(start, len));
            if (prev_is_minus)
                val = -val;
            vector<string> try_plus, try_minus, try_mult;
            if (prev_is_mult) {
                val *= prev_mult_val;
            }

            if (val == target && start+len == num.size())
                return {num.substr(start, len)};

            try_plus = dfs(num, start+len, false, false, NULLINT, target - val);
            try_minus = dfs(num, start+len, true, false, NULLINT, target - val);
            try_mult = dfs(num, start+len, false, true, val, target);

            for (string s : try_plus)
                res.push_back(num.substr(start, len) + "+" + s);
            for (string s : try_minus)
                res.push_back(num.substr(start, len) + "-" + s);
            for (string s : try_mult)
                res.push_back(num.substr(start, len) + "*" + s);
            if (num.at(start) == '0')
                break;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    auto res = sol.addOperators("00", 0);
    res = sol.addOperators("3456237490", 9191);
    for (auto s : res)
        cout << s << endl;
}