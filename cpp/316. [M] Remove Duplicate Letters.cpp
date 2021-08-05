#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <list>
#include <stack>
#include <unordered_set>

using namespace std;;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        stack<char> stk;
        unordered_map<char, int> m;
        unordered_set<char> set;

        for (char c : s) {
            if (m.find(c) == m.end()) {
                m[c] = 0;
            }
            m[c]++;
        }

        for (char c : s) {
            // cout << c << "00000" << endl;
            if (set.find(c) != set.end()) {
                m[c]--;
                continue;
            }
            // cout << c << "11111" << endl;
            while (!stk.empty() && stk.top() >= c && m[stk.top()]) {
                cout << stk.top() << m[stk.top()] << endl;
                set.erase(stk.top());
                stk.pop();
            }
            stk.push(c);
            set.insert(c);
            m[c]--;
        }

        string res = "";
        while (!stk.empty()) {
            res = stk.top() + res;
            stk.pop();
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    cout << sol.removeDuplicateLetters("bcabc") << endl;
    cout << sol.removeDuplicateLetters("cbacdcbc") << endl;
    cout << sol.removeDuplicateLetters("bbcaac") << endl;
}