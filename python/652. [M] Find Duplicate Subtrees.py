# https://leetcode-cn.com/problems/find-duplicate-subtrees/

# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to
# return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure
# with the same node values.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-duplicate-subtrees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        d = {}
        res = []

        def traverse(node: TreeNode) -> (str, str):
            if node is None: return 'x', 'x'
            l_pre, l_ino = traverse(node.left)
            r_pre, r_ino = traverse(node.right)
            pre = str(node.val) + l_pre + r_pre
            ino = l_ino + str(node.val) + r_ino
            key = pre + ';' + ino
            if key in d and d[key] is not None:
                d[key] = None
                res.append(node)
            elif key not in d:
                d[key] = node
            return pre, ino

        traverse(root)
        return res



if __name__ == '__main__':
    sol = Solution()
    # print(sol.checkInclusion("ADO", 'ADDDDDAO'))
    # print(sol.checkInclusion("ADOR", 'ADDDDDAO'))

