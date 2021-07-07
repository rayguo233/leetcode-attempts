# https://leetcode-cn.com/problems/unique-binary-search-trees/

# Given an integer n, return the number of structurally unique
# BST's (binary search trees) which has exactly n nodes of unique
# values from 1 to n.
#
# 1 <= n <= 19
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def __init__(self):
        self.memo = None

    def numTrees(self, n: int) -> int:
        def findNum(m):
            if m == 1: return 1
            res = 0
            for i in range(1, m + 1):
                res += self.memo[i - 1] * self.memo[m - i]
            return res
        self.memo = [1] * (n + 1)
        for i in range(1, n + 1):
            self.memo[i] = findNum(i)
        return self.memo[n]

if __name__ == '__main__':
    sol = Solution()
    # print(sol.merge([[1,2]]))
    assert(sol.numTrees(1) == 1)
    print(sol.numTrees(2))
    print(sol.numTrees(3))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
