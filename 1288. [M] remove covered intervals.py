# https://leetcode-cn.com/problems/remove-covered-intervals/

# Given a list of intervals, remove all intervals that
# are covered by another interval in the list.
#
# Interval [a,b) is covered by interval [c,d) if and
# only if c <= a and b <= d.
#
# After doing so, return the number of remaining intervals.
#
# 1 <= intervals.length
# 0 <= intervals[i][0]
# All the intervals are unique.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-covered-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        left, right = -1, -1
        res = len(intervals)
        for itv in intervals:
            if itv[1] <= right:
                res -= 1
                continue
            if left == itv[0]:
                res -= 1
            left, right = itv[0], itv[1]
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeCoveredIntervals([[1,2]]))
    print(sol.removeCoveredIntervals([[1,2],[0,9],[6,7]]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
