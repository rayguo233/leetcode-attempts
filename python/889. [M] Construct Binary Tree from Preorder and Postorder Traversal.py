import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        left_num_child = postorder.index(preorder[1])

        return TreeNode(preorder[0],
                        self.constructFromPrePost(preorder[1:2+left_num_child],
                                                  postorder[:left_num_child+1]),
                        self.constructFromPrePost(preorder[2+left_num_child:],
                                                  postorder[1+left_num_child:-1]))



if __name__ == '__main__':
    sol = Solution()
