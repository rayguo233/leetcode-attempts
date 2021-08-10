#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;;

class Solution {
public:
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        const int kBuy = 0, kSell = 1;
        priority_queue<int> buyq;
        priority_queue<int, vector<int>, greater<int>> sellq;
        unordered_map<int, int> buym, sellm;
        for (auto const &v : orders) {
            int price = v[0], amt = v[1];
            if (v[2] == kBuy) {
                while (!sellq.empty() && sellq.top() <= price && amt) {
                    int amt_for_sale = sellm[sellq.top()];
                    sellm[sellq.top()] = max(amt_for_sale - amt, 0);
                    amt = max(amt - amt_for_sale, 0);
                    if (sellm[sellq.top()] == 0) {
                        sellm.erase(sellq.top());
                        sellq.pop();
                    }
                }
                if (amt) {
                    buym[price] += amt;
                    if (buym[price] == amt)
                        buyq.push(price);
                }
                continue;
            }
            while (!buyq.empty() && buyq.top() >= price && amt) {
                int amt_buy = buym[buyq.top()];
                buym[buyq.top()] = max(amt_buy - amt, 0);
                amt = max(amt - amt_buy, 0);
                if (buym[buyq.top()] == 0) {
                    buym.erase(buyq.top());
                    buyq.pop();
                }
            }
            if (amt) {
                sellm[price] += amt;
                if (sellm[price] == amt)
                    sellq.push(price);
            }
        }
        int res = 0;
        for (auto const &[key, val] : sellm)
            res = (res + val) % ((int)pow(10, 9) + 7);//, cout << key << ":" << val << endl;
        for (auto const &[key, val] : buym)
            res = (res + val) % ((int)pow(10, 9) + 7);//, cout << key << ":" << val << endl;
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{10,5,0},{15,2,1},{25,1,1},{30,4,0}};
    v = {{7,1000000000,1},{15,3,0},{5,999999995,0},{5,1,1}};
    cout << sol.getNumberOfBacklogOrders(v) << endl;
    // cout << sol.integerBreak(2) << endl;
    // cout << sol.integerBreak(3) << endl;
    // cout << sol.integerBreak(4) << endl;
}