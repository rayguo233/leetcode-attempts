
#include <vector>
#include <string>
#include <iostream>

using namespace std;;

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1)
            return "1";
        string s = countAndSay(n-1);
        char prevC = s.at(0);
        int prevI = 0;
        int len = s.size();
        string res = "";
        for (int i = 1; i < len; i++) {
            if (s.at(i) == prevC)
                continue;
            res += to_string(i - prevI);
            res += prevC;
            prevC = s.at(i);
            prevI = i;
        }
        if (s.at(len-1) == prevC) {
            res += to_string(len - prevI);
            res += prevC;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.countAndSay(5) << endl;
}