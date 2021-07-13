#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
#include <string>
#include <memory>
#include <unordered_set>

using namespace std;;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (!root)
            return {};
        res.push_back(root->val);
        traverse(root->left, res, 1);
        traverse(root->right, res, 1);
        return res;
    }

    void traverse(TreeNode* root, vector<int> &res, int level) {
        if (!root)
            return;
        if (level < res.size()) {
            res[level] = root->val;
        } else {
            assert(level == res.size());
            res.push_back(root->val);
        }
        traverse(root->left, res, level+1);
        traverse(root->right, res, level+1);
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
}