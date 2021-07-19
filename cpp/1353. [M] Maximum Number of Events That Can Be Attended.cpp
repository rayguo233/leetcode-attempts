// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_set>
#include <assert.h>
#include <iostream>
#include <queue>

using namespace std;;

class Compare {
public:
    bool operator() (vector<int> a, vector<int> b) {
        if (a[1] < b[1])
            return false;
        if (a[1] > b[1])
            return true;
        return a[0] > b[0];
    }
};

class Solution {
public:
    int maxEventsSlow(vector<vector<int>>& events) {
        int size = events.size();
        int next_avail_day = 1;
        int res = 0;
        sort(events.begin(), events.end(), compare);
        priority_queue<vector<int>, vector<vector<int>>, Compare> can_attend = {};
        for (vector<int> e : events) {
            while (e[0] > next_avail_day && !can_attend.empty()) {
                vector<int> to_attend = can_attend.top();
                can_attend.pop();
                if (to_attend[1] >= next_avail_day) {
                    next_avail_day++;
                    res++;
                }
            }
            can_attend.push(e);
            if (e[0] > next_avail_day) {
                assert(can_attend.size() == 1);
                next_avail_day = e[0];
            }
        }
        while (!can_attend.empty()) {
            vector<int> to_attend = can_attend.top();
            can_attend.pop();
            if (to_attend[1] >= next_avail_day) {
                next_avail_day++;
                res++;
            }
        }
        return res;
    }

    int maxEvents(vector<vector<int>>& events) {
        int size = events.size();
        int next_avail_day = 1;
        int res = 0;
        sort(events.begin(), events.end());
        priority_queue<int, vector<int>, greater<int>> can_attend = {};
        for (vector<int> e : events) {
            while (e[0] > next_avail_day && !can_attend.empty()) {
                int to_attend = can_attend.top();
                can_attend.pop();
                if (to_attend >= next_avail_day) {
                    next_avail_day++;
                    res++;
                }
            }
            can_attend.push(e[1]);
            if (e[0] > next_avail_day) {
                assert(can_attend.size() == 1);
                next_avail_day = e[0];
            }
        }
        while (!can_attend.empty()) {
            int to_attend = can_attend.top();
            can_attend.pop();
            if (to_attend >= next_avail_day) {
                next_avail_day++;
                res++;
            }
        }
        return res;
    }
private:
    bool static compare(vector<int> a, vector<int> b) {
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
    vector<vector<int>> v = {{1,2},{2,3},{3,4}};
    cout << sol.maxEvents(v) << endl;
}