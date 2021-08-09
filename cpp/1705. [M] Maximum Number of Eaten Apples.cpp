// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <queue>

using namespace std;;

class Solution {
public:
    int eatenApples(const vector<int>& apples, const vector<int>& days) {
        priority_queue<int, vector<int>, greater<int>> q;
        unordered_map<int, int> m;
        const int size = apples.size();
        int day;
        int res = 0;
        for (day = 0; day < size || !q.empty(); ++day) {
            if (day < size) {
                q.push(day + days[day]);
                m[day + days[day]] += apples[day];
            }
            while (!q.empty() && (q.top() <= day || m[q.top()] == 0))
                q.pop();
            if (!q.empty()) {
                res++;
                cout << q.top() << ":" << m[q.top()] << " ";
                m[q.top()]--;
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> ap = {2,1,10};
    vector<int> da = {2,10,1};
    sol.eatenApples(ap, da);
}