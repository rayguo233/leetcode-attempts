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

class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        while (root) {
            m_stack.push_back(root);
            root = root->left;
        }
    }
    
    int next() {
        assert(m_stack.size() > 0);
        TreeNode *nextNode = m_stack.back();
        m_stack.pop_back();
        TreeNode *addNode = nextNode->right;
        while (addNode) {
            m_stack.push_back(addNode);
            addNode = addNode->left;
        }
        return nextNode->val;
    }
    
    bool hasNext() {
        return m_stack.size() > 0;
    }  
private:
    vector<TreeNode*> m_stack = {};
};

int main() {
}