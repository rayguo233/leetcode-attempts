#include <vector>  
#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        int size1 = firstList.size(), size2 = secondList.size();
        vector<vector<int>> intersections = {};
        int i1 = 0, i2 = 0;
        while (i1 < size1 && i2 < size2) {
            vector<int> itv1 = firstList[i1], itv2 = secondList[i2];
            // if no overlap
            if (itv1[1] < itv2[0]) {
                i1++;
                continue;
            }
            if (itv2[1] < itv1[0]) {
                i2++;
                continue;
            }
            // if there is overlap
            intersections.push_back({max(itv1[0], itv2[0]), min(itv1[1], itv2[1])});
            if (itv1[1] < itv2[1])
                i1++;
            else
                i2++;
        }
        return intersections;
    }
};

int main() {
    Solution sol = Solution();
}