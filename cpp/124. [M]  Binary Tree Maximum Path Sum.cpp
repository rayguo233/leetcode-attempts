// https://leetcode.com/problems/binary-tree-maximum-path-sum/

#include <vector>  
#include <iostream>
#include <unordered_map>

using namespace std;


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
    int maxPathSum(TreeNode* root) {
        int maxi = root->val;
        MaxThroughRoot(root, maxi);
        return maxi;
    }
private:
    int MaxThroughRoot(TreeNode *root, int &maxi) {
        if (!root) {
            return 0;
        }
        int left_max = MaxThroughRoot(root->left, maxi);
        int right_max = MaxThroughRoot(root->right, maxi);
        int val = root->val;
        int max_ending_at_root = max(max(val, left_max + val), right_max + val);
        maxi = max(max(maxi, max_ending_at_root), left_max + right_max + val);
        return max_ending_at_root;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> c = {1,2,3,4};
}