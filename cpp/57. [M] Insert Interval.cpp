#include <vector>  
#include <math.h>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> Insert(vector<vector<int>>& intervals, vector<int>& new_interval) {
        const int kItvSize = intervals.size();
        for (int i = 0; i < kItvSize; ++i) {
            vector<int> curr_itv = intervals[i];
            if (curr_itv[1] < new_interval[0])
                continue;
            if (new_interval[1] < curr_itv[0]) {
                intervals.insert(intervals.begin() + i, new_interval);
                return intervals;
            }
            int j;
            for (j = i; j < kItvSize && intervals[j][0] <= new_interval[1]; j++) {
                new_interval[0] = min(new_interval[0], intervals[j][0]);
                new_interval[1] = max(new_interval[1], intervals[j][1]);
            }
            intervals.erase(intervals.begin() + i, intervals.begin() + j);
            intervals.insert(intervals.begin() + i, new_interval);
            return intervals;
        }
        intervals.push_back(new_interval);
        return intervals;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> a;
    a = {{3},{2}};
}