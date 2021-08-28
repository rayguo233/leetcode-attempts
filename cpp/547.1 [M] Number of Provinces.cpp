#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
#include <string>
#include <memory>
#include <unordered_set>

using namespace std;;

#define is_connected isConnected
#define FindCircleNum findCircleNum
 
class Solution {
public:
    int FindCircleNum(vector<vector<int>>& is_connected) {
        const int kN = is_connected.size();
        int parent[kN];
        for (int i = 0; i < kN; ++i)
            parent[i] = i;
        for (int i = 0; i < kN; ++i) {
            for (int j = 0; j < i; ++j) {
                if (is_connected[i][j] == 0 || parent[i] == j)
                    continue;
                int root_i = ConnectToSmallestParent(parent, i);
                int root_j = ConnectToSmallestParent(parent, j);
                parent[max(root_i, root_j)] = min(root_i, root_j);
                parent[i] = min(root_i, root_j);
            }
        }
        int res = 0;
        for (int i = 0; i < kN; ++i) {
            res += parent[i] == i;
        }
        return res;
    }
private:
    int ConnectToSmallestParent(int parent[], int i) {
        if (parent[i] != parent[parent[i]])
            parent[i] = ConnectToSmallestParent(parent, parent[i]);
        return parent[i];
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
    sol.findCircleNum(v);
}