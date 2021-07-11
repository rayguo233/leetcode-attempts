// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_set>
#include <assert.h>
#include <iostream>
#include <cctype>

using namespace std;;

class Solution {
public:
    string decodeString(string s) {
        int start = -1;
        int len = s.length();
        int freq = 0;
        int innerBracket = 0;
        string res = "";
        for (int i = 0; i < len; i++) {
            char c = s.at(i);
            if (start != -1) {
                if (c == ']' && innerBracket == 0) {
                    string subs = decodeString(s.substr(start, i - start));
                    for (int f = 0; f < freq; f++)
                        res += subs;
                    start = -1;
                    freq = 0;
                } else if (c == ']') {
                    innerBracket--;
                } else if (c == '[') {
                    innerBracket++;
                }
            } else {
                if (isdigit(c)) {
                    freq = 10 * freq + (c - '0');
                } else if (c == '[') {
                    start = i + 1;
                } else {
                    res += c;
                }
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.decodeString("1[s15[df]]") << endl;
}