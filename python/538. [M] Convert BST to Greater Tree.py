# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/

# Given the root of a Binary Search Tree (BST), convert it to
# a Greater Tree such that every key of the original BST is
# changed to the original key plus sum of all keys greater than
# the original key in BST.
#
# As a reminder, a binary search tree is a tree that satisfies
# these constraints:
#
# The left subtree of a node contains only nodes with keys less
# than the node's key.
# The right subtree of a node contains only nodes with keys
# greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.summ = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None: return root
        self.convertBST(root.right)
        self.summ += root.val
        root.val = self.summ
        self.convertBST(root.left)
        return root


if __name__ == '__main__':
    sol = Solution()
    # print(sol.invertTree([2,1,4]))
    # assert(sol.invertTree([1,2,1,2]) == 1)
