// https://leetcode.com/problems/container-with-most-water/

#include <math.h>
#include <iostream>

using namespace std;

 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) 
        : val(x), left(left), right(right) {}
 };

class Solution {
public:
    int goodNodes(TreeNode* root) {
        if (!root)
            return 0;
        return traverse(root, root->val);
    }

    int traverse(TreeNode* root, int maxi) {
        if (!root)
            return 0;
        int validRoot = root->val >= maxi;
        maxi = max(maxi, root->val);
        return validRoot + traverse(root->left, maxi) + traverse(root->right, maxi);
    }
};

int main() {
    Solution sol = Solution();
}