// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    int minDeletions(string s) {
        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++;
        }
        sort(freq.begin(), freq.end(), greater<int>());
        int res = 0;
        int prev_freq = INT_MAX;
        for (int f : freq) {
            if (f == 0)
                break;
            // if (prev_freq == -1) {
            //     prev_freq = f;
            //     continue;
            // }
            if (prev_freq > f) {
                prev_freq = f;
                continue;
            }
            res += f - prev_freq + 1;
            prev_freq = max(1, prev_freq-1);
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.minDeletions("bbcebab") << endl;
}