# https://leetcode-cn.com/problems/validate-binary-search-tree/
#
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre = - float('inf')
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, mini, maxi):
            if node is None: return True
            if node.val <= mini or node.val >= maxi: return False
            if node.left is not None and node.left.val >= node.val: return False
            if node.right is not None and node.right.val <= node.val: return False
            return helper(node=node.left, mini=mini, maxi=node.val) and helper(node=node.right, mini=node.val, maxi=maxi)

        return helper(root, - float('inf'), float('inf'))

    def isValidBST_try2(self, root: TreeNode) -> bool:
        if root is None: return True
        if not self.isValidBST_try2(root.left): return False
        if root.val <= self.pre: return False
        return self.isValidBST_try2(root.right)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    head = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
    assert(head is not None)
    stack = [head]
    while stack:
        curr = stack.pop(0)
        print(curr.val)
        if curr.left is not None: stack.append(curr.left)
        if curr.right is not None: stack.append(curr.right)

    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)