# https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree/

# Given a binary tree root, the task is to return the
# maximum sum of all keys of any sub-tree which is
# also a Binary Search Tree (BST).
#
# The given binary tree will have between 1 and 40000 nodes.
# Each node's value is between [-4 * 10^4, 4 * 10^4].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

INF = float('inf')
class Solution:
    def __init__(self):
        self.res = 0

    def maxSumBST(self, root: TreeNode) -> int:

        def sum_bst(node: TreeNode, mini, maxi) -> (float, float, float):
            if node is None: return 0, None, None
            l_sum, l_min, l_max = sum_bst(node.left, mini, node.val)
            r_sum, r_min, r_max = sum_bst(node.right, node.val, maxi)
            if node.left is None: l_min, l_max = node.val, node.val
            if node.right is None: r_min, r_max = node.val, node.val
            self.res = max(self.res, l_sum, r_sum)
            if node.left is not None and l_max >= node.val: return - INF, INF, - INF
            if node.right is not None and r_min <= node.val: return - INF, INF, - INF
            return l_sum + node.val + r_sum, l_min, r_max

        self.res = max(sum_bst(root, - INF, INF)[0], self.res)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.merge([[1,2]]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
