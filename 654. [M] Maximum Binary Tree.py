# https://leetcode-cn.com/problems/maximum-binary-tree/

# You are given an integer array nums with no duplicates.
# A maximum binary tree can be built recursively from nums
# using the following algorithm:
#
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to
# the left of the maximum value.
#
# Recursively build the right subtree on the subarray suffix to
# the right of the maximum value.
# Return the maximum binary tree built from nums.
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # rank: 97.41; 28.73

    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        root = TreeNode(val=nums[0])
        stack = [root]
        for num in nums[1:]:
            curr = TreeNode(val=num)
            left = None
            while stack and stack[-1].val < num:
                left = stack.pop(-1)
            if not stack:
                assert(left is not None)
                assert(left == root)
                curr.left = root
                root = curr
            elif left is None:
                stack[-1].right = curr
            else:
                curr.left = left
                stack[-1].right = curr
            stack.append(curr)

        return root



if __name__ == '__main__':
    sol = Solution()
    # print(sol.checkInclusion("ADO", 'ADDDDDAO'))
    # print(sol.checkInclusion("ADOR", 'ADDDDDAO'))
    ptr = sol.constructMaximumBinaryTree([1,2,3,6,0,5])
    stack = [ptr]
    curr = None
    print(1)
    while len(stack) > 0 or curr is not None:
        if curr is not None:
            print(curr.val)
            stack += [curr.left, curr.right]
        curr = stack.pop(0) if stack else None
