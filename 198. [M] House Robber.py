# https://leetcode-cn.com/problems/house-robber/

# You are a professional robber planning to rob houses
# along a street. Each house has a certain amount of money
# stashed, the only constraint stopping you from robbing each
# of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent
# houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money
# of each house, return the maximum amount of money you can rob
# tonight without alerting the police.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def rob(self, nums: list[int]) -> int:
        dp_rob, dp_safe = [0] * 2, [0] * 2
        cur_house = 0
        for n in nums:
            dp_rob[cur_house], dp_safe[cur_house] = max(dp_safe[not cur_house] + n, dp_rob[cur_house] + n), \
                                                    max(dp_safe[not cur_house], dp_rob[not cur_house])
            cur_house = not cur_house
        return max(dp_rob[not cur_house],  dp_safe[not cur_house])

if __name__ == '__main__':
    sol = Solution()
    assert(sol.rob([0]) == 0)
    assert(sol.rob([2,1,4]) == 6)
    assert(sol.rob([2,4]) == 4)
    assert(sol.rob([2,1,4,8]) == 10)
    assert(sol.rob([2,1,4,8,9]) == 15)
