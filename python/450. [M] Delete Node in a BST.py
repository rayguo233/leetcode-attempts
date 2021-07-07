# https://leetcode-cn.com/problems/delete-node-in-a-bst/

# Given a root node reference of a BST and a key, delete
# the node with the given key in the BST. Return the root
# node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Follow up: Can you solve it with time complexity
# O(height of tree)?
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.parent = None

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.parent = None
        nodeDel = self.findNode(root, key)
        if nodeDel is None: return root

        # if `nodeDel` is a leaf
        if nodeDel.left is None and nodeDel.right is None:
            if self.parent is None:
                return None
            if self.parent.right == nodeDel:
                self.parent.right = None
            else:
                self.parent.left = None
        # if non-leaf with 2 children
        elif nodeDel.left is not None and nodeDel.right is not None:
            self.insertRight(nodeDel.left, nodeDel.right)
            if self.parent is None:
                return nodeDel.left
            if self.parent.right == nodeDel:
                self.parent.right = nodeDel.left
            else:
                self.parent.left = nodeDel.left
        # if non-leaf with 1 children
        else:
            child = nodeDel.left if nodeDel.left is not None else nodeDel.right
            if self.parent is None:
                return child
            if self.parent.right == nodeDel:
                self.parent.right = child
            else:
                self.parent.left = child

        return root

    def findNode(self, root, key) -> TreeNode:
        if root is None: return None
        if root.val == key: return root

        self.parent = root
        if root.val < key: return self.findNode(root.right, key)
        if root.val > key: return self.findNode(root.left, key)

    def insertRight(self, root, insertNode):
        if root.right is None:
            root.right = insertNode
        else:
            self.insertRight(root.right, insertNode)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.invertTree([2,1,4]))
    # assert(sol.invertTree([1,2,1,2]) == 1)
