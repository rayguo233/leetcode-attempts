// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>
#include <map>
#include <iterator>

using namespace std;

#define num_smaller(itr) (itr->second.first)
#define num_larger(itr) (itr->second.second)

class Solution {
public:
    int numTeams(vector<int>& rating) {
        int size = rating.size();
        int res = 0;
        map<int, pair<int, int>> m;
        for (int i = 0; i < size; i++) {
            int r = rating[i];
            m[r] = {0, 0};
            auto it_curr = m.find(r);
            int num_small = distance(m.begin(), it_curr);
            int num_large = i - num_small;
            m[r] = {num_small, num_large};
            // find number of backword decreasing triplets
            for (auto it_small = m.begin(); it_small != it_curr; it_small++) {
                res += num_smaller(it_small);
            }
            // find number of backword increasing triplets
            auto it_end = m.end();
            auto it_large = it_curr;
            for (it_large++; it_large != it_end; it_large++) {
                res += num_larger(it_large);
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {};
    cout << sol.numTeams(a) << endl;
    a = {1};
    cout << sol.numTeams(a) << endl;
    a = {1,2,4};
    cout << sol.numTeams(a) << endl;
    a = {1,2,4,6};
    cout << sol.numTeams(a) << endl;
}