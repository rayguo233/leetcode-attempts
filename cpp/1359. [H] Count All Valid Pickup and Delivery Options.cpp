// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <math.h>

using namespace std;;

class Solution {
public:
    int countOrders(int n) {
        unsigned long long int res = 1;
        const int maxi = pow(10, 9) + 7;
        for (int curr_max_num = 1; curr_max_num < n; curr_max_num++) {
            const int addition = (2*curr_max_num + 1) * curr_max_num + 2*curr_max_num + 1;
            // cout << curr_max_num << "-----" << endl;
            const int orig_res = res;
            // res = 0;
            // for (int i = 0; i < addition-1; i += 2) {
            //     res = res + (orig_res * 2) % maxi;
            // }
            // res = (res + (orig_res * (addition % 2))) % maxi;
            res = (res * addition) % maxi;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.countOrders(1) << endl;
    cout << sol.countOrders(2) << endl;
    cout << sol.countOrders(3) << endl;
    cout << sol.countOrders(4) << endl;
    cout << sol.countOrders(8) << endl;
}