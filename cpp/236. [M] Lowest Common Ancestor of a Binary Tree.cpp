// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <math.h>
#include <iostream>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 

class Solution {
private:
    TreeNode* m_res = nullptr;
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        traverse(root, p, q);
        return m_res;
    }

    int traverse(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || m_res)
            return 0;
        int sum = traverse(root->left, p, q) + traverse(root->right, p, q) + (root == p || root == q);
        if (sum == 2)
            m_res = root;
        return sum;
    }
};

int main() {
    Solution sol = Solution();
}