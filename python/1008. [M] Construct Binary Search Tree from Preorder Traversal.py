import bisect
import sys
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode(sys.maxsize)
        stack = [dummy]
        for val in preorder:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
                continue
            while len(stack) > 2 and val < stack[-2].val:
                stack.pop()
            stack[-1].right = node
            stack.append(node)
        return dummy.left

if __name__ == '__main__':
    sol = Solution()
    print(sol.bstFromPreorder([1,2,3,4,3,5,2]), -1)
