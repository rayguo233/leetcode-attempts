# https://leetcode-cn.com/problems/house-robber-ii/

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

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        res = 0
        for houses in (nums[:-1], nums[1:]):
            # print(houses)
            cur_index = 0
            dp_rob, dp_safe = [0] * 2, [0] * 2
            for h in houses:
                dp_rob[cur_index], dp_safe[cur_index] = max(dp_safe[not cur_index] + h, dp_rob[cur_index] + h), \
                                                        max(dp_safe[not cur_index], dp_rob[not cur_index])
                cur_index = not cur_index
            res = max(dp_rob[not cur_index], dp_safe[not cur_index], res)

        return res

if __name__ == '__main__':
    sol = Solution()
    assert(sol.rob([0]) == 0)
    assert(sol.rob([2,1,4]) == 4)
    assert(sol.rob([2,4]) == 4)
    assert(sol.rob([2,1,4,8]) == 9)
    assert(sol.rob([2,1,4,8,9]) == 13)
