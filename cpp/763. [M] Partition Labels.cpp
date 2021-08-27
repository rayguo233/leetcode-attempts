#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
#include <string>
#include <memory>
#include <unordered_set>
#include <queue>

using namespace std;;

class Comp {
    bool operator() (pair<int, int> a, pair<int, int> b) {
        return a.first == b.first ? a.second > b.second : a.first < b.first;
    }
};

class Solution {
public:
    vector<int> partitionLabels(const string s) {
        vector<pair<int, int>> p(26, {INT_MAX, INT_MIN});
        for (int i = 0; i < s.size(); i++) {
            int c = s[i] - 'a';
            p[c] = {min(i, p[c].first), max(i, p[c].second)};
        }
        auto compare = [](const pair<int, int> &a, const pair<int, int> &b) -> bool {
            return a.first == b.first ? a.second > b.second : a.first < b.first;
        };
        sort(p.begin(), p.end(), compare);
        vector<int> res;
        int start = -1, end = -1;
        for (auto &pr : p) {
            if (pr.first == INT_MAX)
                return res;
            if (start == -1) {
                start = pr.first, end = pr.second;
                continue;
            }
            if (pr.first > end) {
                res.push_back(end - start + 1);
                start = pr.first, end = pr.second;
                continue;
            }
            end = pr.second;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
}