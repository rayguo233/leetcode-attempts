# Definition for a binary tree node.
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def find_max_depth(rt: TreeNode, curr_depth) -> int:
            if rt is None:
                return curr_depth - 1
            return max(find_max_depth(rt.left, curr_depth + 1), find_max_depth(rt.right, curr_depth+1))

        self.res = None
        max_depth = find_max_depth(root, 0)
        print(max_depth)
        
        def num_deepest_sides(node: TreeNode, curr_depth: int) -> int:
            if curr_depth - 1 == max_depth:
                return 1
            if node is None: 
                return 0
            print(node.val, curr_depth)
            num_good_subtree = (num_deepest_sides(node.left, curr_depth+1) > 0) + (num_deepest_sides(node.right, curr_depth+1) > 0)
            if num_good_subtree == 2:
                self.res = node
            return num_good_subtree

        num_deepest_sides(root, 0)
        return self.res



if __name__ == '__main__':
    s = Solution()
    print(s.lexicalOrder(4))
    print(s.lexicalOrder(12))
    print(s.lexicalOrder(20))
    print(s.lexicalOrder(29))
    print(s.lexicalOrder(126))