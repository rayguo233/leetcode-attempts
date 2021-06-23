# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    c = 0

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def build(l_pre, r_pre, l_in, r_in) -> TreeNode:  # [l_pre, r_pre], [l_in, r_in]
            # if self.c > 15: return
            # self.c += 1
            # print(l_pre, r_pre, l_in, r_in)
            if l_pre > r_pre:
                return None

            curr = TreeNode(val=preorder[l_pre])
            if l_pre == r_pre:
                return curr

            ind = inorder.index(curr.val)
            l_span = ind - l_in
            r_span = r_in - ind

            curr.left = build(l_pre + 1, l_pre + l_span, l_in, ind - 1)
            curr.right = build(l_pre + l_span + 1, l_pre + l_span + r_span, ind + 1, ind + r_span)

            return curr

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    head = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
    assert(head is not None)
    stack = [head]
    while stack:
        curr = stack.pop(0)
        print(curr.val)
        if curr.left is not None: stack.append(curr.left)
        if curr.right is not None: stack.append(curr.right)

    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)