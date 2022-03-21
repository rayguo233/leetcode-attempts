# Definition for a binary tree node.
from turtle import left
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def get_sum_and_depth(node: Optional[TreeNode], depth: int) -> Tuple[int, int]:
            if node is None:
                return 0, 0
            left_sum, left_depth = get_sum_and_depth(node.left, depth + 1)
            right_sum, right_depth = get_sum_and_depth(node.right, depth + 1)
            if left_depth == right_depth:
                max_depth = left_depth
                max_sum = left_sum + right_sum
            elif left_depth < right_depth:
                max_depth = right_depth
                max_sum = right_sum
            else:
                max_depth = left_depth
                max_sum = left_depth
            if max_depth == 0:
                return node.val, depth
            return max_sum, max_depth
        
        return get_sum_and_depth(root)[0]
            

        

if __name__ == '__main__':
    sol = Solution()
    print(sol.countPairs([1048576,1048576]))
