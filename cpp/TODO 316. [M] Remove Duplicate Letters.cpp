#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <list>

using namespace std;;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        list<char> l;
        unordered_map<char, pair<list<char>::iterator, bool>> m;

        for (char c : s) {
            if (m.find(c) == m.end()) {
                l.push_back(c);
                auto end = l.end();
                end--;
                m[c] = {end, false};
                // cout << *(m[c]) << endl;
                assert((*(m[c].first)) == c);
                continue;
            }

            auto c_pos = m[c].first;
            auto itr = c_pos;
            itr++;
            if (itr != l.end() && (*itr) < c) {
                itr--;
                l.erase(itr);
                l.push_back(c);
                auto end = l.end();
                end--;
                m[c] = {end, false};
                continue;
            }
            assert((*itr) != c);
        }

        string res = "";
        for (char c : l)
            res += c;
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    cout << sol.removeDuplicateLetters("bcabc") << endl;
    cout << sol.removeDuplicateLetters("cbacdcbc") << endl;
}