# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the
# shortest path from the root node down to the nearest leaf node.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = [root]
        cur_level_size = len(stack)
        cur_level = 0

        while True:
            for _ in range(cur_level_size):
                node = stack.pop(0)
                if node is None: continue
                if node.left is None and node.right is None:
                    return cur_level + 1
                stack += [node.left, node.right]
            cur_level += 1
            cur_level_size = len(stack)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    assert(sol.minDepth(TreeNode()) == 1)
    assert(sol.minDepth(None) == 0)
    assert(sol.minDepth(TreeNode(0,TreeNode(),TreeNode())) == 2)
    assert(sol.minDepth(TreeNode(0,TreeNode(),TreeNode(0,TreeNode()))) == 2)

    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)