// https://leetcode.com/problems/decode-ways-ii/

#include <vector>  
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

#define STAR -1

class Solution {
public:
    int numDecodingsFailed(string s) {
        int len = s.size();
        if (len == 0 || s.at(0) == '0')
            return 0;
        int prev2, prev1, prevDigit;
        processFirstDigit(prev2, prev1, prevDigit, s.at(0));

        for (int i = 1; i < len; i++) {
            int currDigit;
            s.at(i) == '*' ? currDigit = STAR : currDigit = s.at(i) - '0';
            if (currDigit == 0 && (prevDigit > 2 || prevDigit == 0)) // this is why STAR != 10
                return 0;
            processDigit(prev2, prev1, prevDigit, currDigit);
        }
        return prev1;
    }

    void processDigit(int &prev2, int &prev1, int &prevDigit, int currDigit) {
        int curr;
        if (currDigit == 0) {
            curr = prev2;
            if (prevDigit == STAR)
                curr *= 2;
        } else if (currDigit == STAR) {
            curr = prev1 * 9;
            if (prevDigit == 1)
                curr += prev2 * 9;
            else if (prevDigit == 2)
                curr += prev2 * 6;
            else if (prevDigit == STAR)
                curr += prev2 * 17;
        } else {
            curr = prev1;
            if (prevDigit == STAR) {
                if (currDigit <= 6)
                    curr += prev2 * 2;
                else
                    curr += prev2;
            }
            else if (prevDigit == 1 || (prevDigit == 2 && currDigit <= 6))
                curr += prev2;
        } 
        curr %= int(pow(10, 7) + 7);
        prev2 = prev1;
        prev1 = curr;
        prevDigit = currDigit;
    }

    void processFirstDigit(int &prev2, int &prev1, int &prevDigit, char currChar) {
        if (currChar == '*') {
            prev2 = 1;
            prev1 = 9;
            prevDigit = STAR;
        } else {
            prev2 = 1;
            prev1 = 1;
            prevDigit = currChar - '0';
        }
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.numDecodingsFailed("*******") << endl;
}