// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

#define Combine combine

class Solution {
public:
    vector<vector<int>> Combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> comb(k, 1);
        for (int i = 0; i < k; i++)
            comb[i] = i+1;
        while (comb[k-1] <= n || (comb[k-1] = Backtrack(comb, k-2, n, k) + 1) != 0) {
            vector<int> next(comb);
            res.push_back(next);
            comb[k-1]++;
        }
        return res;
    }
private:
    int Backtrack(vector<int> &comb, int i, int n, int k) {
        if (i == -1)
            return -1;
        if (comb[i] == n - k + i + 1 && (comb[i] = Backtrack(comb, i-1, n, k)) == -1)
            return -1;
        comb[i]++;
        return comb[i];
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<int> ::iterator ptr;
}