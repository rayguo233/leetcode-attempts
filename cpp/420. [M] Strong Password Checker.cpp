// https://leetcode.com/problems/strong-password-checker/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <math.h>

using namespace std;;

#define RANDOM_CHAR ';'

class Solution {
public:
    int strongPasswordChecker(string password) {
        int len = password.size();
        bool need_lower = true, need_upper = true, need_digit = true;
        int num_discrete_repeat = 0;
        int num_consec_repeat = 0;
        int num_consec_repeat_group = 0;
        pair<char, int> prev_char = {RANDOM_CHAR, 0};

        for (char c : password) {
            if (isdigit(c))
                need_digit = false;
            if (islower(c))
                need_lower = false;
            if (isupper(c))
                need_upper = false;
            if (c == prev_char.first) {
                prev_char.second++;
                if (prev_char.second % 3 == 0) {
                    num_discrete_repeat += prev_char.second == 3;
                    num_discrete_repeat -= prev_char.second == 6;
                    num_consec_repeat += prev_char.second != 3;
                    num_consec_repeat += prev_char.second == 6;
                    num_consec_repeat_group += prev_char.second == 6;
                }
                continue;
            }
            prev_char = {c, 1};
        }

        int total_needs = need_lower + need_upper + need_digit;
        if (len < 6) {
            int num_add = 6 - len;
            return max(num_add, total_needs);
        }
        if (len > 20) {
            int num_del = len - 20;
            num_discrete_repeat = max(0, num_discrete_repeat - num_del);
            if (num_del - num_discrete_repeat > 0) {
                num_consec_repeat = max(0, num_consec_repeat - (num_del - num_discrete_repeat + 2) / 3);
            }
            return num_del + max(num_discrete_repeat + num_consec_repeat, total_needs);
        }
        return max(num_discrete_repeat + num_consec_repeat, total_needs);
    }
};

int main() {
    Solution sol = Solution();
    string a = "FFFFFFFFFFFFFFF11111111111111111111AAA";
    a = "bbaaaaaaaaaaaaaaacccccc";
    cout << "5 6+2 3" << endl;
    cout << a.size() << endl;
    cout << sol.strongPasswordChecker(a) << endl;
}