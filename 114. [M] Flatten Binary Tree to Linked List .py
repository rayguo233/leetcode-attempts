# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class where
# the right child pointer points to the next node in the list
# and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order
# traversal of the binary tree.
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None: return None

        cur = root
        stack = [root.right, root.left]
        while cur is not None or len(stack) > 0:
            nex = stack.pop(-1)
            while nex is None and len(stack) > 0: nex = stack.pop(-1)
            cur.left, cur.right = None, nex
            cur = nex
            if nex is not None: stack += [nex.right, nex.left]


if __name__ == '__main__':
    sol = Solution()
    # print(sol.invertTree([2,1,4]))
    # assert(sol.invertTree([1,2,1,2]) == 1)
