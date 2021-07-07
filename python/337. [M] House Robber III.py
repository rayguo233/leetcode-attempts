# https://leetcode-cn.com/problems/house-robber-iii/

# You are a professional robber planning to rob houses
# along a street. Each house has a certain amount of
# money stashed. All houses at this place are arranged
# in a circle. That means the first house is the neighbor
# of the last one. Meanwhile, adjacent houses have a
# security system connected, and it will automatically
# contact the police if two adjacent houses were broken
# into on the same night.
#
# Given an integer array nums representing the amount
# of money of each house, return the maximum amount of
# money you can rob tonight without alerting the police.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

ROB = 0
SAFE = 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(node: TreeNode) -> tuple[int, int]:
            if node is None: return 0, 0

            l, r = dp(node.left), dp(node.right)
            rob = node.val + l[SAFE] + r[SAFE]
            safe = max(l) + max(r)
            return rob, safe

        return max(dp(root))


if __name__ == '__main__':
    sol = Solution()
    # assert(sol.rob([2,1,4]) == 4)
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
