# Definition for a binary tree node.
import sys
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.max_diff = 0

        def get_child_min_max(node: Optional[TreeNode]) -> List[int]:
            if node is None:
                return [sys.maxsize, -1]
            child_min_max = get_child_min_max(node.left) + get_child_min_max(node.right) + [node.val]
            child_min_max = [min(child_min_max, key=lambda x: sys.maxsize if x == -1 else x),
                             max(child_min_max, key=lambda x: -1 if x == sys.maxsize else x)]
            self.max_diff = max([abs(extreme - node.val) for extreme in child_min_max if extreme not in [-1, sys.maxsize]] + [self.max_diff])
            return child_min_max
        
        get_child_min_max(root)
        return self.max_diff


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxAncestorDiff(TreeNode(1)))