# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/

# Given an integer n, return all the structurally unique
# BST's (binary search trees), which has exactly n nodes of
# unique values from 1 to n. Return the answer in any order.
#
# 1 <= n <= 8
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        def copy_tree(tree, add) -> TreeNode:
            if tree is None: return None
            return TreeNode(val=tree.val + add, left=copy_tree(tree.left, add), right=copy_tree(tree.right, add))

        def copy_trees(trees: [TreeNode], add: int) -> list[TreeNode]:
            if add == 0: return trees
            return [copy_tree(tree, add) for tree in trees]

        record = {0: [None]}  # type: dict[int: [TreeNode]]
        for num_nodes in range(1, n + 1):
            trees = []
            for head_val in range(1, num_nodes + 1):
                left_trees = record[head_val - 1]
                right_trees = copy_trees(trees=record[num_nodes - head_val], add=head_val)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        trees.append(TreeNode(val=head_val, left=left_tree, right=right_tree))
            record[num_nodes] = trees
        return record[n]



if __name__ == '__main__':
    sol = Solution()
    # print(sol.merge([[1,2]]))
    assert(sol.numTrees(1) == 1)
    print(sol.numTrees(2))
    print(sol.numTrees(3))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
