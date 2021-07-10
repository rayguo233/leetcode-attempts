// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>
#include <unordered_map>

using namespace std;


class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        unordered_map<int, int> m;
        int rem, need;
        int res = 0;
        for (int t : time) {
            rem = t % 60;
            rem == 0 ? need = 0 : need = 60 - rem;
            if (m.find(need) != m.end()) {
                res += m[need];
            }
            if (m.find(rem) == m.end()) {
                m[rem] = 1;
            } else
                m[rem]++;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a;
    a = {60,60};
    cout << sol.numPairsDivisibleBy60(a) << endl;
}