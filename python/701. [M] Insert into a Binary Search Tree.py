# https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/

# You are given the root node of a binary search tree
# (BST) and a value to insert into the tree. Return the root
# node of the BST after the insertion. It is guaranteed that the
# new value does not exist in the original BST.
#
# Notice that there may exist multiple valid ways for the
# insertion, as long as the tree remains a BST after insertion.
# You can return any of them.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val=val)
        curr = root
        while True:
            assert(curr is not None)
            # look to the left
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val=val)
                    break
                else:  # val < curr.left.val
                    curr = curr.left
            # look to the right
            else:  # val > curr.val
                if curr.right is None:
                    curr.right = TreeNode(val=val)
                    break
                else:  # val > curr.right.val
                    curr = curr.right
        return root


if __name__ == '__main__':
    sol = Solution()
    # print(sol.invertTree([2,1,4]))
    # assert(sol.invertTree([1,2,1,2]) == 1)
