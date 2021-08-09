#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <queue>

using namespace std;;

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        typedef pair<int, int> p;
        sort(classes.begin(), classes.end(), [](const vector<int> &a, const vector<int> &b) -> bool {
            return a[1] == b[1] ? a[0] > b[0] : a[1] > b[1];});
        const int size = classes.size();
        int init_val = extraStudents - 1;
        while (extraStudents && extraStudents != init_val) {
            init_val = extraStudents;
            for (int i = 0; i < size && extraStudents; ++i) {
                if (classes[i][0] == classes[i][1])
                    continue;
                while (extraStudents && (i == size-1 || classes[i][1] <= classes[i+1][1])) {
                    classes[i][0]++;
                    classes[i][1]++;
                    extraStudents--;
                }
            }
        }
        double res = 0;
        for (vector<int> &v : classes) {
            res += v[0] / (double)v[1];
        }
        return res / size;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> s = {{4,6},{3,9},{6,7},{2,10}};
    cout << sol.maxAverageRatio(s, 0) << endl;
}