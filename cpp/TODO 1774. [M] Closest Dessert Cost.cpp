#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <queue>
#include <utility>
#include <cstdlib>

using namespace std;;

class Solution {
public:
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        priority_queue<int, vector<int>, greater<int>> top_costs;
        int topping_size = toppingCosts.size();
        for (int first = 0; first < topping_size; ++first) {
            int second = first;
            top_costs.push(toppingCosts[first]);
            while (second < topping_size) {
                top_costs.push(toppingCosts[first] + toppingCosts[second]);
                second++;
            }
        }
        sort(baseCosts.begin(), baseCosts.end(), greater<int>());
        int res = baseCosts[0] + top_costs.top() - target;
        const int base_size = baseCosts.size();
        for (int i = 0; i < base_size; ++i) {
            int base = baseCosts[i];
            while (!top_costs.empty() && (base + top_costs.top()) <= target) {
                cout << base << " " << top_costs.top() << endl;
                if (i && abs(baseCosts[i-1] + top_costs.top() - target) < abs(res))
                    res = baseCosts[i-1] + top_costs.top() - target;
                if (abs(base + top_costs.top() - target) < abs(res))
                    res = base + top_costs.top() - target;
                top_costs.pop();
            }
        }
        return res + target;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> v1 = {2,3};
    vector<int> v2 = {4,5,100};
    cout << sol.closestCost(v1, v2, 18) << endl;
    // cout << sol.integerBreak(2) << endl;
    // cout << sol.integerBreak(3) << endl;
    // cout << sol.integerBreak(4) << endl;
}