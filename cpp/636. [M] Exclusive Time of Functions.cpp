#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
#include <string>

using namespace std;;


class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> res(n, 0);
        vector<pair<int, int>> stack;
        int prevEnd = -1;
        for(string s : logs) {
            int pos = s.find(':');
            int i = stoi(s.substr(0, pos));
            s.erase(0, pos + 1);
            pos = s.find(':');
            bool start = s.substr(0, pos) == "start";
            int t = stoi(s.substr(pos+1, s.length()));

            if (start) {
                if (stack.size()) {
                    if (prevEnd < stack.back().second) {
                        res[stack.back().first] += t - stack.back().second;
                    } else {
                        res[stack.back().first] += t - prevEnd - 1;
                    }
                }
                stack.push_back({i, t});
                continue;
            }
            if (prevEnd < stack.back().second) {
                res[stack.back().first] += t + 1 - stack.back().second;
            } else {
                res[stack.back().first] += t - prevEnd;
            }
            prevEnd = t;
            stack.pop_back();
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<string> s = {"0:start:0","1:start:2","1:end:5","0:end:6"};
    vector<int> r = sol.exclusiveTime(2, s);
    for (int i : r) {
        cout << i << ' ';
    }
    cout << endl;
}