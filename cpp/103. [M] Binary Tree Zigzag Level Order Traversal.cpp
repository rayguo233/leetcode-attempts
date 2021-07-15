// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root)
            return {};
        vector<TreeNode*> currLevel = {root};
        vector<TreeNode*> nextLevel;
        vector<vector<int>> res;
        bool leftToRight = true;
        while (currLevel.size() > 0) {
            nextLevel = {};
            res.push_back({});
            int size = currLevel.size();
            for (int i = 0; i < size; i++) {
                TreeNode *getNextLevNode = currLevel[i];
                TreeNode *getValNode;
                leftToRight ? getValNode = getNextLevNode : getValNode = currLevel[size-1-i];
                res.back().push_back(getValNode->val);
                if (getNextLevNode->left)
                    nextLevel.push_back(getNextLevNode->left);
                if (getNextLevNode->right)
                    nextLevel.push_back(getNextLevNode->right);
            }
            leftToRight = !leftToRight;
            currLevel.swap(nextLevel);
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
}