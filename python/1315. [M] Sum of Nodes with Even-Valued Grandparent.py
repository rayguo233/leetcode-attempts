# Definition for a binary tree node.
from turtle import left


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumEvenGrandparent(self,
                           root: TreeNode,
                           is_p_even=False,
                           is_gp_even=False) -> int:
        if root is None:
            return 0
        is_root_even = root.val % 2 == 0
        return self.sumEvenGrandparent(
            root.left, is_root_even, is_p_even) + self.sumEvenGrandparent(
                root.right, is_root_even, is_p_even) + root.val * is_gp_even


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubarray([2, 1, 4], 4))
    print(sol.longestSubarray([2, 1, 4, 1], 1))
    print(sol.longestSubarray([2, 1, 4, 1], 0))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
