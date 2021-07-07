# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

# Given the root of a binary search tree, and an
# integer k, return the kth (1-indexed) smallest
# element in the tree.
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        def traverse(node: TreeNode):
            if node is None: return -1
            left = traverse(node.left)
            if left >= 0: return left
            if self.k == 1: return node.val
            self.k -= 1
            return traverse(node.right)

        return traverse(root)






if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('sdffssdfgghjk'))
    print(sol.lengthOfLongestSubstring('sdfsdfs'))
    print(sol.lengthOfLongestSubstring(''))
