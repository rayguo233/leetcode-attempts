#include <vector>
#include <set>
#include <queue>
#include <utility>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        int res = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (auto v : reservedSeats) {
            if (v[1] != 1 && v[1] != 10) {
                pq.push({v[0], v[1]});
                if (v[0] == 3)
                    cout << v[1] << "ssss" << endl;
            }
        }
        for (int r = 1; r <= n; ++r) {
            int left = 1, right = 1, center = 1;
            if (!pq.empty() && pq.top().first == r && pq.top().second < 4) {
                left = 0;
                while (!pq.empty() && pq.top().first == r && pq.top().second < 4)
                    pq.pop();
            }
            if (!pq.empty() && pq.top().first == r && pq.top().second < 6) {
                left = 0, center = 0;
                while (!pq.empty() && pq.top().first == r && pq.top().second < 6)
                    pq.pop();                    
            }
            if (!pq.empty() && pq.top().first == r && pq.top().second < 8) {
                right = 0, center = 0;
                while (!pq.empty() && pq.top().first == r && pq.top().second < 8)
                    pq.pop();
            }
            if (!pq.empty() && pq.top().first == r && pq.top().second < 10) {
                right = 0;
                while (!pq.empty() && pq.top().first == r && pq.top().second < 10)
                    pq.pop();
            }
            res += max(left + right, center);
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{4,7},{4,1},{3,1},{5,9},{4,4},{3,7},
        {1,3},{5,5},{1,6},{1,8},{3,9},{2,9},{1,4},{1,9},{1,10}};
    cout << sol.maxNumberOfFamilies(5, v) << endl;
}