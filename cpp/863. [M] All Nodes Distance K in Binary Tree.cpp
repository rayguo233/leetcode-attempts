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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int> res;
        traverse(root, target, k, res);
        return res;
    }
private:
    int traverse(TreeNode* root, TreeNode* target, int k, vector<int> &res) {
        if (!root)
            return -1;
        // root is target
        if (root == target) {
            kFromRoot(root, k, res);
            return 1;
        }
        int left, right;
        left = traverse(root->left, target, k ,res);
        // root is distance k from target on the left
        if (left == k) {
            res.push_back(root->val);
            return left + 1;
        }
        // root is more than distance k from target on the left
        if (left > k) {
            return left + 1;
        }
        // root is less than distance k from target on the left
        if (left > 0) {
            kFromRoot(root->right, k - left - 1, res);
            return left + 1;
        }

        // now that target is not found on the left
        assert(left == -1);
        right = traverse(root->right, target, k ,res);

        // root is distance k from target on the right
        if (right == k) {
            res.push_back(root->val);
            return right + 1;
        }
        // root is more than distance k from target on the left
        if (right > k) {
            return right + 1;
        }
        // root is less than distance k from target on the right
        if (right > 0) {
            kFromRoot(root->left, k - right - 1, res);
            return right + 1;
        }
        // target not under root
        return -1;
    }

    void kFromRoot(TreeNode* root, int k, vector<int> &res) {
        if (!root || k < 0)
            return;
        if (k == 0) {
            res.push_back(root->val);
            return;
        }
        kFromRoot(root->left, k-1, res);
        kFromRoot(root->right, k-1, res);
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
}