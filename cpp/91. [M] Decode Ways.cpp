// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>
#include <string>

using namespace std;


class Solution {
public:
    int numDecodings(string s) {
        int len = s.size();
        if (len == 0 || s.at(0) == '0')
            return 0;
        int prev2 = 1, prev1 = 1, prevDigit = s.at(0) - '0';

        for (int i = 1; i < len; i++) {
            int currDigit = s.at(i) - '0';
            if (currDigit == 0 && (prevDigit > 2 || prevDigit == 0))
                return 0;
            processDigit(prev2, prev1, prevDigit, currDigit);
        }
        return prev1;
    }

    void processDigit(int &prev2, int &prev1, int &prevDigit, int currDigit) {
        int curr = prev1;
        if (currDigit == 0) {
            curr = prev2;
        }
        // cout << prevDigit << ' ' << currDigit << endl;
        else if (prevDigit == 1 || (prevDigit == 2 && currDigit <= 6)) {
            curr += prev2;
        }
        prev2 = prev1;
        prev1 = curr;
        prevDigit = currDigit;
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.numDecodings("102") << endl;
}