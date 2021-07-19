// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_set>
#include <assert.h>
#include <iostream>
#include <queue>

using namespace std;;

class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        int size = events.size();
        sort(events.begin(), events.end(), compare);
        int res = 0;
        queue<vector<int>> not_attended = {};
        int last_attend_day = 0;
        for (vector<int> e : events) {
            while (!not_attended.empty() && not_attended.front()[1] <= e[1]) {
                vector<int> to_attend = not_attended.front();
                not_attended.pop();
                if (to_attend[1] > last_attend_day) {
                    last_attend_day++;
                }
            }
        }
    }
private:
    bool compare(vector<int> a, vector<int> b) {
        if (a[0] < b[0]) {
            return true;
        }
        if (a[0] == b[0]) {
            if (a[1] < b[1])
                return true;
            return false;
        }
        return false;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{1,0}};
}