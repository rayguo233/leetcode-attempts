// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int minCost(string s, vector<int>& cost) {
        int totalCost = 0;
        int maxCost = cost.at(0);
        char prevChar = s.at(0);
        int len = s.size();
        for (int i = 1; i < len; i++) {
            int currCost = cost.at(i);
            char currChar = s.at(i);
            if (currChar != prevChar) {
                prevChar = currChar;
                maxCost = currCost;
                continue;
            }
            if (currCost > maxCost) {
                totalCost += maxCost;
                maxCost = currCost;
                continue;
            }
            totalCost += currCost;
        }
        return totalCost;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> c = {1,2,3,4};
    cout << sol.minCost("aaaa", c) << endl;
}