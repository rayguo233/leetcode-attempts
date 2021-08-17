// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int res = 0;
        int si = 0;
        for (int need : g) {
            while (si < s.size() && need > s[si])
                si++;
            if (si == s.size())
                return res;
            res++;
            si++;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    // cout << sol.integerBreak(2) << endl;
    // cout << sol.integerBreak(3) << endl;
    // cout << sol.integerBreak(4) << endl;
}