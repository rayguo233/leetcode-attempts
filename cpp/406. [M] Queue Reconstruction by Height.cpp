#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <list>

using namespace std;;

class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        auto compare = [](const vector<int> &a, const vector<int> &b) -> bool {
            return a[1] == b[1] ? a[0] < b[0] : a[1] < b[1];
        };
        sort(people.begin(), people.end(), compare);
        list<vector<int>> l;
        for (vector<int> p : people) {
            int k = p[1], h = p[0];
            auto itr = l.begin();
            for (; itr != l.end() && k; itr++) {
                if ((*itr)[0] >= h)
                    k--;
            }
            while (itr != l.end() && ((*itr)[0] < h)) {
                itr++;
            }
            l.insert(itr, p);
        }
        vector<vector<int>> res;
        for (vector<int> v : l)
            res.push_back(v);
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {10,2};
}