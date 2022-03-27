import bisect
import collections
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = collections.deque([root])
        curr_lev = 1
        min_lev = 0
        max_sum = - 10 ** 6
        while dq:
            curr_sum = 0
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
                curr_sum += node.val
            if curr_sum > max_sum:
                max_sum = curr_sum
                min_lev = curr_lev
            curr_lev += 1
        return min_lev

if __name__ == '__main__':
    sol = Solution()
    print(sol.numPermsDISequence('D'))
    print(sol.numPermsDISequence('DID'))
