import bisect
import itertools
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None and root.val == targetSum:
            return [[targetSum]]
        return [[root.val] + path for path in itertools.chain(self.pathSum(root.left, targetSum - root.val),
                                                              self.pathSum(root.right, targetSum - root.val))]

if __name__ == '__main__':
    sol = Solution()
    print(sol.racecar(1), 1)
    print(sol.racecar(2), 4)
    print(sol.racecar(3), 2)
    print(sol.racecar(6))
